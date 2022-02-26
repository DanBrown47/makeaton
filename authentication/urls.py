from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from authentication.views import register_admin, register_user, register_voluntere

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/admin/', register_admin, name='register-admin'),
    path('register/voluntere/', register_voluntere, name='register-voluntere'),
    path('register/user/', register_user, name='register-user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
