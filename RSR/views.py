from django.shortcuts import render, get_object_or_404
# from django.http import Http404

from .models import Ressources, Commentaire


def show_ressource(request, id):
    ressource = get_object_or_404(Ressources, id=id)
    commentaires = Commentaire.objects.all().order_by('-created_at')
    return render(request, 'ressources/show_ressource.html', {'id': ressource, 'commentaires': commentaires})
