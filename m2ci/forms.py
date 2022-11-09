from .models import message
from django.forms import ModelForm
from django import forms

class message_form(forms.ModelForm):
    class Meta:
        model = message
        fields = '__all__'