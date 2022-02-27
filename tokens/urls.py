from django.urls import path
from .views import *

app_name = 'tokens'

urlpatterns = [
    path('', list_token, name='list'),
    path('<int:id>/', detail_token, name='detail'),
    path('create/', create_token, name='create'),
    path('catch-token/', catch_token, name='catch-token'),
    path('complete-token/', complete_token, name='complete-token'),
    path('cancel-token/', cancel_token, name='cancel-token'),
    path('user/', user_tokens, name='user-tokens')
]
