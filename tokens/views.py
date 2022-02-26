from django.shortcuts import redirect, render
import folium
import geocoder
from .forms import TokenForm
from .models import Token
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create_token(request):
    form = TokenForm()
    if request.method == 'POST':
        raised_by = request.user
        images = request.FILES.get('image')
        message = request.POST['message']
        lat = request.POST['lat']
        lng = request.POST['lng']
        Token.objects.create(
            raised_by=raised_by,
            images=images,
            lat=lat,
            lng=lng,
            message=message
        )

    return render(request, 'token_create.html', {'form': form})


def list_token(request):
    tokens = Token.objects.all()
    return render(request, 'token_list.html', {'tokens': tokens})


def detail_token(request, id):
    token = Token.objects.get(id=id)

    return render(request, 'token_detail.html', {'token': token})


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
