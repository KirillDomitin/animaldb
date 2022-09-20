from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from animals.models import ShelterModel
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    shelter = forms.ModelChoiceField(queryset=ShelterModel.objects.all())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AuthForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
       model = Profile
       fields = ['shelter']