from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import Http404

from .models import Ressources, Commentaire, Reponse
from .forms import ReponseForm, CommentaireForm


def show_ressource(request, id):
    ressource = get_object_or_404(Ressources, id=id)
    commentaires = Commentaire.objects.all().order_by('-created_at')
    reponses = Reponse.objects.all().order_by('-created_at')
    form = CommentaireForm
    comment_list = []
    for commentaire in commentaires:
        if ressource.id == commentaire.id_ressources.id:
            comment_list.append(commentaire)
    return render(request, 'ressources/show_ressource.html', {'id': ressource,
                                                              'commentaires': comment_list,
                                                              'reponses': reponses, 'form': form})


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