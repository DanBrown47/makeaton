from django.urls import path
from .views import detail_token, list_token, create_token

app_name = 'tokens'

urlpatterns = [
    path('', list_token, name='list'),
    path('<int:id>/', detail_token, name='detail'),
    path('create/', create_token, name='create')
]
