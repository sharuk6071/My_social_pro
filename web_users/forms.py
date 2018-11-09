from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    gender = forms.CharField(max_length=1)

    class Meta:
        model = User
        fields = ['username', 'email', 'gender','password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    gender = forms.CharField(max_length=1)

    class Meta:
        model = User
        fields = ['username', 'email', 'gender']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
