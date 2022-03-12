from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'ressources'

urlpatterns = [
    re_path('r/(?P<id>[0-9]+)$', views.show_ressource, name='show_ressource'),
    path('administration_ressources', views.admin_list_ressources, name='admin_list_ressources'),
    path('delete_ressource/<int:id>', views.delete_ressources, name="delete_ressource"),
    path('add_ressource', views.add_ressource, name="add_ressource"),
    path('edit_ressource/<int:id>', views.edit_ressource, name="edit_ressource"),
    re_path('update_commentary/(?P<id>[0-9]+)$', views.update_commentary, name='update_commentary'),
    re_path('add_commentary/(?P<id>[0-9]+)$', views.add_commentary, name="add_commentary"),
    re_path('delete_commentary/(?P<id>[0-9]+)$', views.delete_commentary, name="delete_commentary")
]
