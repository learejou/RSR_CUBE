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
    re_path('delete_commentary/(?P<id>[0-9]+)$', views.delete_commentary, name="delete_commentary"),
    re_path('add_favoris/(?P<id>[0-9]+)$', views.add_favoris, name="add_favoris"),
    re_path('delete_favoris/(?P<id>[0-9]+)$', views.delete_favoris, name="delete_favoris"),
    path('activate_ressource/(?P<id>[0-9]+)$', views.activate_ressource, name='activate_ressource'),
    path('delete_category/<int:id>', views.delete_category, name="delete_category"),
    path('add_category', views.add_category, name="add_category"),
    path('administration_users', views.admin_list_users, name='admin_list_users'),
    path('activate_user/<int:id>', views.activate_user, name="activate_user"),
    path('profil/', views.profil, name="profil"),
    path('profil/edit_profil/<int:id>', views.edit_profil, name="edit_profil"),
]
