from django import forms
from django.forms import ModelForm

from .models import Choice


class ChoiceModel(ModelForm):

    class Meta:
        model = Choice
        fields = []
