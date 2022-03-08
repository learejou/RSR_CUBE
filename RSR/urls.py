from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'ressources'

urlpatterns = [
    re_path('r/(?P<id>[0-9]+)$', views.show_ressource, name='show_ressource'),
    path('administration', views.admin_list_ressources, name='admin_list_ressources'),
    path('delete_ressource/<int:id>', views.delete_ressources, name="delete_ressource"),
    path('add_ressource', views.add_ressource, name="add_ressource"),
]
