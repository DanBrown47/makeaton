from django.urls import path
from .views import map, token

app_name = 'tokens'

urlpatterns = [
    path('', token, name='token')
]
