from django.db.models import Sum, QuerySet
from django.shortcuts import render

from Ressources.models import Ressources


def index(request):
    if not request.user.is_authenticated:
        ressources: QuerySet[Ressources] = Ressources.objects.filter(valide=True)
        ressources_valide: QuerySet[Ressources] = ressources
    else:
        ressources = Ressources.objects.all()
        ressources_valide = ressources.filter(valide=True)

    visited_ressource_nb: int = ressources_valide.filter(visits__gt=0).count()

    ressource_nb: int = ressources.count()
    ressource_nb_valid: int = ressources_valide.count()
    sum_visits: int = ressources.aggregate(total=Sum('visits'))['total']

    v = ressources.values('category').annotate(total=Sum('visits'))

    context = {
        'ressource_nb': ressource_nb,
        'ressource_nb_valid': ressource_nb_valid,
        'ressource_nb_invalid': ressource_nb - ressource_nb_valid,
        'visited_ressource_nb': visited_ressource_nb,
        'sum_visits': sum_visits,
        'v': v,
    }
    return render(request, template_name='stats/index.html', context=context)
