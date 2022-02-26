from django.urls import path
from .views import map

app_name = 'tokens'

urlpatterns = [
    path('', map, name='map')
]
