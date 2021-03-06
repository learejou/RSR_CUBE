from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
#from django.http import Http404
from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404

from .forms import EditProfilForm, InputForm, CommentaireForm, RegisterForm
from .models import Ressources, Commentaire, Category, Consulte


def show_ressource(request, id):
    ressource = get_object_or_404(Ressources, id=id)
    if not(request.user.is_staff or request.user.is_superuser):
        ressource.visits += 1
        ressource.save()

    commentaires = Commentaire.objects.all().order_by('created_at')
    form = CommentaireForm
    comment_list = []
    for commentaire in commentaires:
        if ressource.id == commentaire.id_ressources.id:
            comment_list.append(commentaire)
    if request.user.is_authenticated:
        try:
            Consulte.objects.get(id_citoyen=request.user, id_ressources=ressource)
        except ObjectDoesNotExist:
            formConsulte = Consulte(id_citoyen=request.user,
                                    id_ressources=ressource,
                                    exploite=True)
            formConsulte.save()
        consulte = Consulte.objects.get(id_citoyen=request.user, id_ressources=ressource)
        return render(request, 'ressources/show_ressource.html', {'id': ressource,
                                                                  'commentaires': comment_list,
                                                                  'form': form,
                                                                  'consulte': consulte})
    return render(request, 'ressources/show_ressource.html', {'id': ressource,
                                                              'commentaires': comment_list,
                                                              'form': form})


def profil(request):
    ressources = Ressources.objects.all().order_by('-created_at')
    listfav = []
    listexploi = []
    listcreer = []
    profil = get_object_or_404(User, id=request.user.id)
    form = EditProfilForm(request.POST or None, instance=profil)
    form_pass = PasswordChangeForm(request.user, request.POST)
    for ressource in ressources:
        if request.user == ressource.auteur :
            listcreer.append(ressource)
        try:
            consultes = Consulte.objects.filter(id_citoyen=request.user)
            for consulte in consultes:
                if ressource == consulte.id_ressources and consulte.favoris == True:
                    listfav.append(ressource)
                if ressource == consulte.id_ressources and consulte.exploite == True:
                    listexploi.append(ressource)
        except ObjectDoesNotExist:
           return render(request, 'pages/profil.html', {'fav': listfav, 'exploi': listexploi, 'creer': listcreer, 'form':form, 'form_pass':form_pass}) 
                
    return render(request, 'pages/profil.html', {'favs': listfav, 'explois': listexploi, 'creers': listcreer, 'form':form, 'form_pass':form_pass})


def edit_profil(request):
    profil_user = get_object_or_404(User, id=request.user.id)
    form = EditProfilForm(request.POST or None, instance=profil_user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil modifi?? avec succ??s !')
            return(profil(request))

    return(profil(request))


def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Mot de passe chang?? avec succ??s ! ')
        else:
            messages.error(request, 'Il y a une erreur dans le nouveau mot de passe.')
    return(profil(request))

def admin_list_ressources(request):
    ressources = Ressources.objects.all().order_by('-created_at')
    categories = Category.objects.all().order_by('name')
    return render(request, 'administration/admin_list_ressources.html',
                  {'ressources': ressources, 'categories': categories})


def admin_list_users(request):
    User = get_user_model()
    utilisateurs = User.objects.all()
    return render(request, 'administration/admin_list_users.html', {'utilisateurs': utilisateurs})


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
    return (admin_list_users(request=request))


def add_ressource(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        titre = form.data['titre']
        stockage = form.data['stockage']
        category = Category.objects.get(pk=form.data['category'])
        form = Ressources(titre=titre,
                          auteur=request.user,
                          stockage=stockage,
                          valide=1,
                          category=category)
        form.save()
        messages.success(request, ('Ressource ajouter avec succ??s'))
        return render(request, 'administration/add_ressource.html', {'form': InputForm()})
    else:
        form = InputForm()

    return render(request, 'administration/add_ressource.html', {'form': form})


def edit_ressource(request, id):
    ressource = get_object_or_404(Ressources, id=id)
    form = InputForm(request.POST or None, instance=ressource)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            if request.user == ressource.auteur:
                ressource.valide = 1
                ressource.save()
            return (show_ressource(request=request, id=id))

    return render(request, 'administration/edit_ressource.html', {
        'id': ressource,
        'form': form,
    })


def activate_ressource(request, id):
    if request.POST['active'] == "activer":
        active = 2
    else:
        active = 1
    ressource = get_object_or_404(Ressources, id=id)
    ressource.valide = active
    ressource.save()
    return (show_ressource(request=request, id=id))

def refuse_ressource(request, id):
    ressource = get_object_or_404(Ressources, id=id)
    ressource.valide = 0
    ressource.save()
    return (admin_list_ressources(request=request))
    
def delete_ressources(request, id):
    deleteObject = get_object_or_404(Ressources, id=id)
    deleteObject.delete()
    ressources = Ressources.objects.all().order_by('-created_at')
    categories = Category.objects.all().order_by('name')
    messages.success(request, ('Ressource supprimer.'), {})
    return render(request, 'administration/admin_list_ressources.html', {'ressources': ressources, 'categories':categories})


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
    return (show_ressource(request=request, id=ressource.id))


def update_commentary(request, id):
    commentaire = Commentaire.objects.get(pk=id)
    form = CommentaireForm(request.POST or None, instance=commentaire)
    if form.is_valid():
        form.save()
        return (show_ressource(request=request, id=commentaire.id_ressources.id))
    return render(request, 'ressources/update_commentary.html', {'commentaire': commentaire, 'form': form})


def delete_commentary(request, id):
    commentaire = get_object_or_404(Commentaire, id=id)
    commentaires = Commentaire.objects.all()
    for reponse in commentaires:
        if reponse.fromcom == commentaire.id:
            reponse.delete()
    id = commentaire.id_ressources.id
    commentaire.delete()
    return (show_ressource(request=request, id=id))


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return (admin_list_ressources(request=request))


def add_category(request):
    name = request.POST['name']
    form = Category(name=name)
    form.save()
    return (admin_list_ressources(request=request))


def add_favoris(request, id):
    ressource = Ressources.objects.get(pk=id)
    consulte = Consulte.objects.get(id_citoyen=request.user, id_ressources=ressource)

    consulte.favoris = True
    consulte.save()
    return (show_ressource(request=request, id=ressource.id))


def delete_favoris(request, id):
    ressource = Ressources.objects.get(pk=id)
    consulte = Consulte.objects.get(id_citoyen=request.user, id_ressources=ressource)

    consulte.favoris = False
    consulte.save()
    return (show_ressource(request=request, id=ressource.id))
