from .models import Reponse, Commentaire, Ressources
from tkinter import Widget
from tkinter.tix import Form
from django import forms
from django.forms import ModelForm


class InputForm(forms.ModelForm):
    class Meta:
        model = Ressources
        fields = ('titre', 'stockage')

        Widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'stockage': forms.TextInput(attrs={'class': 'form-control'})
        }


class ReponseForm(ModelForm):
    class Meta:
        model = Reponse
        fields = ('auteur', 'reponse')


class CommentaireForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ('commentaire',)
        labels = {
            'commentaire': ''
        }

        widgets = {
            'commentaire': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'commentaire'})
        }
