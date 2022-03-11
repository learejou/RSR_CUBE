from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
#from django.http import Http404
from django.contrib import messages

from .forms import InputForm, ReponseForm, CommentaireForm
from .models import Ressources, Commentaire, Reponse


def show_ressource(request, id):
    ressource = get_object_or_404(Ressources, id=id)
    return render(request, 'ressources/show_ressource.html', {'id': ressource})


def admin_list_ressources(request):
    ressources = Ressources.objects.all().order_by('-created_at')
    return render(request, 'administration/admin_list_ressources.html', {'ressources': ressources})


def add_ressource(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        titre = form.data['titre']
        stockage = form.data['stockage']
        form = Ressources(titre=titre, auteur=request.user.username, stockage=stockage, valide=True)
        form.save()
        messages.success(request, ('Ressource ajouter avec succès'))
        return render(request, 'administration/add_ressource.html', {'form':InputForm()})
    else:
        form = InputForm()
    
    return render(request, 'administration/add_ressource.html', {'form':form})

def edit_ressource(request, id):
    ressource = get_object_or_404(Ressources, id=id)
    form = InputForm(request.POST or None, instance=ressource)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return(show_ressource(request=request, id=id))
            
    return render(request, 'administration/edit_ressource.html', {
        'id': ressource,
        'form':form,
        })


def delete_ressources(request, id):
    deleteObject = get_object_or_404(Ressources, id=id)
    deleteObject.delete()
    ressources = Ressources.objects.all().order_by('-created_at')
    messages.success(request, ('Ressource supprimer.'), {})
    return render(request, 'administration/admin_list_ressources.html', {'ressources': ressources})

def update_commentary(request, id):
    commentaire = Commentaire.objects.get(pk=id)
    form = CommentaireForm(request.POST or None, instance=commentaire)
    if form.is_valid():
        form.save()
        return show_ressource(request=request, id=commentaire.id_ressources.id)
    return render(request, 'ressources/update_commentary.html', {'commentaire': commentaire, 'form': form})


def add_commentary(request, id):
    if request.method == "POST":
        form = CommentaireForm(request.POST)
        commentaire = form.data['commentaire']
        date = datetime.now()
        name = "Billy"
        ressource = Ressources.objects.get(pk=id)
        form = Commentaire(id_ressources=ressource, auteur=name,
                           commentaire=commentaire, date=date)
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))