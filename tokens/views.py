from django.shortcuts import render
import folium
import geocoder
# Create your views here.


def map(request):
    # form = MyGeoForm()
    address = 'kinassery' #the address that want to display in page
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    print(lat, '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    # Create Map Object
    map = folium.Map(location=[19, -12], zoom_start=2)

    folium.Marker([lat, lng], tooltip='Click for more',
                  popup=country).add_to(map)
    # Get HTML Representation of Map Object
    map = map._repr_html_()
    return render(request, 'map.html', {'map' : map})
