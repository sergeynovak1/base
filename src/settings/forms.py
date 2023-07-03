from django import forms
from .models import SystemSettings


class EditSettingForm(forms.ModelForm):
    class Meta:
        model = SystemSettings
        fields = ('value', 'description')
