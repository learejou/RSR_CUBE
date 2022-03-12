from .models import Commentaire, Ressources, Category
from tkinter import Widget
from tkinter.tix import Form
from django import forms
from django.forms import ModelForm


class InputForm(forms.ModelForm):
    class Meta:
        model = Ressources
        fields = ('titre', 'stockage','category')

        category_list = Category.objects.all()

        Widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'stockage': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.ChoiceField(choices=category_list)
        }


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
