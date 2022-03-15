from django.contrib import admin

from .models import *


# Register your models here.

@admin.register(Ressources)
class RessourcesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)
    list_display = ('titre', 'auteur', 'visits', 'created_at', 'updated_at')
    list_filter = ('auteur', 'valide', 'created_at')


admin.site.register(Consulte)
admin.site.register(Commentaire)
admin.site.register(Category)
