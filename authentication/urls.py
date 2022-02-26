from django.urls import path
from django.contrib.auth.views import LoginView

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]
