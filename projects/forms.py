from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username', 'first_name', 'email', 'password1', 'password2'}

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

