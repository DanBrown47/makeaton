from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()


class AdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class VoluntereCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
