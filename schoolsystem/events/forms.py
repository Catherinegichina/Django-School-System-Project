from django import forms
from django.forms import fields
from .models import Events
class EventsRegistrationForm(forms.ModelForm):
    class Meta:
        model=Events
        fields="__all__"