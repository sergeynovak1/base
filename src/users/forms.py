from django import forms
from .models import User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role')


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password']