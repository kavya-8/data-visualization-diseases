from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from .models import User


class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets={'username': forms.TextInput(attrs={'class': 'form-control'}),
                 'password': forms.PasswordInput(attrs={'class': 'form-control'})}



