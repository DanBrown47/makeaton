from django.shortcuts import redirect, render
import folium
import geocoder

from tokens.forms import TokenForm
from .models import CatchToken, Token
from django.contrib.auth.decorators import login_required
from authentication.models import User

# Create your views here.


@login_required
def create_token(request):
    if request.method == 'POST':
        raised_by = request.user
        number = request.POST['number']
        images = request.FILES.get('image')
        message = request.POST['message']
        lat = request.POST['lat']
        lng = request.POST['lng']
        category = request.POST['category']
        Token.objects.create(
            raised_by=raised_by,
            images=images,
            lat=lat,
            lng=lng,
            message=message,
            number=number,
            category=category
        )
        return redirect('../')
    return render(request, 'token_create.html')


@login_required
def list_token(request):
    tokens = Token.objects.all()
    return render(request, 'token_list.html', {'tokens': tokens})


@login_required
def detail_token(request, id):
    token = Token.objects.get(id=id)
    try:
        catch_token = CatchToken.objects.get(token=token)
        i = 0
        catched_by = catch_token.catched_by
    except:
        i = 1
        catched_by = ''
    context = {
        'token': token, 'id': id, 'i': i, 'catched_by': catched_by, 'user': request.user
    }

    return render(request, 'token_detail.html', context=context)


@login_required
def catch_token(request):
    if request.method == 'POST':
        catch = int(request.POST['catch'])
        user = User.objects.get(username=request.user)
        token = Token.objects.get(id=catch)
        CatchToken.objects.create(
            catched_by=user,
            token=token
        )
        return redirect(f'../{catch}')


def complete_token(request):
    complete = int(request.POST['complete'])
    token = Token.objects.get(id=complete)
    token.is_done = True
    token.save()
    catch_token = CatchToken.objects.get(token=Token.objects.get(id=complete))
    catch_token.delete()
    return redirect(f'../{complete}')


def cancel_token(request):
    cancel = int(request.POST['cancel'])
    catch_token = CatchToken.objects.get(token=Token.objects.get(id=cancel))
    catch_token.delete()
    return redirect(f'../{cancel}')


def user_tokens(request):
    if request.user.is_admin:
        tokens = Token.objects.all()
    elif request.user.is_voluntere:
        print('yeah')
        catch_tokens = CatchToken.objects.filter(catched_by=request.user)

        tokens = []

        for catch_token in catch_tokens:
            tokens.append(catch_token.token)
    else:
        tokens = Token.objects.filter(raised_by=request.user.id)
    context = {'tokens': tokens}
    return render(request, 'user_tokens.html', context)


# def map(request):
#     # form = MyGeoForm()
#     address = 'kinassery' #the address that want to display in page
#     location = geocoder.osm(address)
#     lat = location.lat
#     lng = location.lng
#     country = location.country
#     # Create Map Object
    # map = folium.Map(location=[19, -12], zoom_start=2)

#     folium.Marker([lat, lng], tooltip='Click for more',
#                   popup=country).add_to(map)
#     # Get HTML Representation of Map Object
#     map = map._repr_html_()
#     return render(request, 'map.html')
