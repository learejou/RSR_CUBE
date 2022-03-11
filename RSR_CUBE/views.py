from django.shortcuts import render
from django.contrib import admin

from Ressources.models import Ressources

def home(request):
    ressources = Ressources.objects.all().order_by('-created_at')
    return render(request, 'pages/index.html', {'ressources': ressources})

def contact(request):
    return render(request, 'pages/contact.html')

