from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from members.models import Citoyen


# Create your models here.

# On créer une classe qui récuperera la datetime de quand la donnée est ajouté et quand elle est modifié automatiquement
class TimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Ajoute une classe Meta pour signifier que cette classe n'est pas à mettre en BDD mais elle est utilitaire
    class Meta:
        abstract = True


class Category(TimeModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ressources(TimeModel):
    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    stockage = models.TextField()
    valide = models.IntegerField(default=1)
    visits = models.PositiveIntegerField("Nombre de visites", default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class Consulte(TimeModel):
    id_citoyen = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    id_ressources = models.ForeignKey(Ressources, on_delete=models.CASCADE)
    favoris = models.BooleanField(default=False)
    exploite = models.BooleanField(default=False)
    sauvegarde = models.BooleanField(default=False)

    def __str__(self):
        return self.id_citoyen.username


class Commentaire(TimeModel):
    id_ressources = models.ForeignKey(Ressources, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    commentaire = models.TextField()
    fromcom = models.IntegerField(default=None)

    def __str__(self):
        return self.commentaire
