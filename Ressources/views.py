from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
#from django.http import Http404
from django.contrib import messages
from django.contrib.auth import get_user_model

from .forms import InputForm, CommentaireForm
from .models import Ressources, Commentaire, Category


def show_ressource(request, id):
    ressource = get_object_or_404(Ressources, id=id)
    commentaires = Commentaire.objects.all().order_by('-created_at')
    form = CommentaireForm
    comment_list = []
    for commentaire in commentaires:
        if ressource.id == commentaire.id_ressources.id:
            comment_list.append(commentaire)
    return render(request, 'ressources/show_ressource.html', {'id': ressource,
                                                              'commentaires': comment_list,
                                                              'form': form})


def admin_list_ressources(request):
    ressources = Ressources.objects.all().order_by('-created_at')
    categories = Category.objects.all().order_by('name')
    return render(request, 'administration/admin_list_ressources.html', {'ressources': ressources, 'categories': categories})


def admin_list_users(request):
    User = get_user_model()
    utilisateurs = User.objects.all()
    return render(request, 'administration/admin_list_users.html', {'utilisateurs':utilisateurs})


def activate_user(request, id):
    User = get_user_model()
    utilisateur = get_object_or_404(User, id=id)
    print(utilisateur.is_active)
    if utilisateur.is_active == False:
        active = True
    else:
        active = False
    utilisateur.is_active = active
    utilisateur.save()
    return(admin_list_users(request=request))


def add_ressource(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        titre = form.data['titre']
        stockage = form.data['stockage']
        category = Category.objects.get(pk=form.data['category'])
        form = Ressources(titre=titre, 
                        auteur=request.user, 
                        stockage=stockage, 
                        valide=False, 
                        category=category)
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


def activate_ressource(request, id):
    if request.POST['active'] == "activer":
        active = True
    else:
        active = False
    ressource = get_object_or_404(Ressources, id=id)
    ressource.valide = active
    ressource.save()
    return(show_ressource(request=request, id=id))

def delete_ressources(request, id):
    deleteObject = get_object_or_404(Ressources, id=id)
    deleteObject.delete()
    ressources = Ressources.objects.all().order_by('-created_at')
    messages.success(request, ('Ressource supprimer.'), {})
    return render(request, 'administration/admin_list_ressources.html', {'ressources': ressources})


def add_commentary(request, id):
    form = CommentaireForm(request.POST)
    commentaire = form.data['commentaire']
    if request.method == "POST":
        fromcom = form.data['fromcom']
        name = request.user
        ressource = Ressources.objects.get(pk=id)
        form = Commentaire(id_ressources=ressource, auteur=name,
                           commentaire=commentaire, fromcom=fromcom)
        form.save()
    return(show_ressource(request=request, id=ressource.id))

def update_commentary(request, id):
    commentaire = Commentaire.objects.get(pk=id)
    form = CommentaireForm(request.POST or None, instance=commentaire)
    if form.is_valid():
        form.save()
        return(show_ressource(request=request, id=commentaire.id_ressources.id))
    return render(request, 'ressources/update_commentary.html', {'commentaire': commentaire,'form': form})


def delete_commentary(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)
    commentaires = Commentaire.objects.all()
    for reponse in commentaires:
        if reponse.fromcom == commentaire.id:
            reponse.delete()
    id = commentaire.id_ressources.id
    commentaire.delete()
    return(show_ressource(request=request, id=id))


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()    
    return(admin_list_ressources(request=request))


def add_category(request):
    name = request.POST['name']
    form = Category(name=name)
    form.save()
    return(admin_list_ressources(request=request))
