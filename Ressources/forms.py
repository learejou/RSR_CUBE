from django.forms import ModelForm
from django import forms
from .models import Reponse, Commentaire


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
