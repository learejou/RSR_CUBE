from tkinter import Widget
from tkinter.tix import Form
from django import forms
from django.forms import ModelForm

from RSR.models import Ressources

class InputForm(forms.ModelForm):
    class Meta:
        model = Ressources
        fields = ('titre', 'stockage')

        Widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'stockage': forms.TextInput(attrs={'class':'form-control'})
        }