from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# /!\ Duplication par rapport à Ressources.models mais impossible à import "most likely due to a circular import" /!\
# On créer une classe qui récuperera la datetime de quand la donnée est ajouté et quand elle est modifié automatiquement
class TimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Ajoute une classe Meta pour signifier que cette classe n'est pas à mettre en BDD mais elle est utilitaire
    class Meta:
        abstract = True


class Role(TimeModel):
    libelle = models.CharField(max_length=20)

    def __str__(self):
        return self.libelle


class Groupe(TimeModel):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Citoyen(TimeModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_naissance = models.DateField('Date de naissance', null=True, blank=True)
    actif = models.BooleanField()
    role = models.OneToOneField(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
