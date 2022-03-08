from django import forms

class InputForm(forms.Form):
    titre = forms.CharField(max_length=100)
    stockage = forms.CharField()