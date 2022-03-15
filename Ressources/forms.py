from .models import Commentaire, Ressources, Category
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, modelform_factory


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


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    last_name = forms.CharField(label = "Nom de famille")
    first_name = forms.CharField(label = "Prénom")

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email", )


class EditProfilForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email", )

