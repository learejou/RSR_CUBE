from django.contrib import admin

from .models import Ressources
# Register your models here.
admin.site.register(Ressources)


from .models import Commentaire
# Register your models here.
admin.site.register(Commentaire)


from .models import Reponse
# Register your models here.
admin.site.register(Reponse)