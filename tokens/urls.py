from django.urls import path
from .views import token, token_list

app_name = 'tokens'

urlpatterns = [
    path('', token, name='token'),
    path('token_list/', token_list, name='totoken_listken')
]
