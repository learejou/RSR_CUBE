from django.http import BadHeaderError, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.contrib import messages
from Ressources.forms import ContactForm

from Ressources.models import Ressources

def home(request):
    ressources_recent = Ressources.objects.all().order_by('-created_at')[:6]
    ressources = Ressources.objects.all().order_by('-created_at')
    return render(request, 'pages/index.html', {'ressources_recent': ressources_recent, 'ressources': ressources})

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            titre = form.data['titre']
            from_email = form.data['from_email']
            message = form.data['message']
            try: 
                send_mail(titre, message, from_email, ['yanisremond@outlook.fr'])
                messages.success(request, ('Message envoyé avec succès'))
            except BadHeaderError:
                messages.success(request, ('Une erreur est survenu dans l\'envoie du message'))
                return HttpResponse('Invalide header.')

    return render(request, 'pages/contact.html', {'form':form})

