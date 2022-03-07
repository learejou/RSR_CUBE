from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Citoyen)
admin.site.register(Ressources)
admin.site.register(Consulte)
admin.site.register(Role)
admin.site.register(Groupe)
admin.site.register(Commentaire)
admin.site.register(Reponse)
