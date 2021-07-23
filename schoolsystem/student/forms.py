from django import forms
from django.forms import fields
from .models import Student
# 1--the form rep the model.
# django has lbraries that we need to import.
# Inherits from model forms.
# wat fields we want to show-Meta purpose.
# field-first name,lastname.
# 2-views.-puts the form in a http request.
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"