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


class Ressources(TimeModel):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    stockage = models.TextField()
    valide = models.BooleanField()

    def __str__(self):
        return self.titre


class Consulte(TimeModel):
    id_citoyen = models.ForeignKey(Citoyen, on_delete=models.CASCADE)
    id_ressources = models.ForeignKey(Ressources, on_delete=models.CASCADE)
    favoris = models.BooleanField()
    exploite = models.BooleanField()
    sauvegarde = models.BooleanField()

    def __str__(self):
        return self.id_citoyen


class Commentaire(TimeModel):
    id_ressources = models.ForeignKey(Ressources, on_delete=models.CASCADE)
    auteur = models.CharField(max_length=100)
    commentaire = models.TextField()

    def __str__(self):
        return self.id_com

class Reponse(TimeModel):
    id_commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE)
    auteur = models.CharField(max_length=100)
    reponse = models.TextField()

    def __str__(self):
        return self.auteur
