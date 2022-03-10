from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'ressources'

urlpatterns = [
    re_path('r/(?P<id>[0-9]+)$', views.show_ressource, name='show_ressource'),
    re_path('update_commentary/(?P<id>[0-9]+)$', views.update_commentary, name='update_commentary'),
    re_path('add_commentary/(?P<id>[0-9]+)$', views.add_commentary, name="add_commentary")
]
