from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    re_path('p/(?P<id>[0-9]+)/$', views.show, name='show'),
    #Ou alors :
    # path('posts/<int:id>', views.show),
]
