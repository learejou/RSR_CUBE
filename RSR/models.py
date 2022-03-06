from django.db import models


# Create your models here.

# On créer une classe qui récuperera la datetime de quand la donnée est ajouté et quand elle est modifié automatiquement
class TimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Ajoute une classe Meta pour signifier que cette classe n'est pas à mettre en BDD mais elle est utilitaire
    class Meta:
        abstract = True


class Citoyen(TimeModel):
    id_Citoyen = models.BigAutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Date_naissance = models.DateField('Date de naissance')
    Mail = models.EmailField(max_length=75)
    Actif = models.BooleanField()


class Ressources(TimeModel):
    id_Ressources = models.BigAutoField(primary_key=True)
    Titre = models.CharField(max_length=100)
    Auteur = models.CharField(max_length=100)
    Stockage = models.CharField(max_length=500)
    Valide = models.BooleanField()


class Consule(TimeModel):
    id_Citoyen = models.ForeignKey(Citoyen, on_delete=models.CASCADE)
    id_Ressources = models.ForeignKey(Ressources, on_delete=models.CASCADE)
    Favoris = models.BooleanField()
    Exploite = models.BooleanField()
    Sauvegarde = models.BooleanField()


class Role(TimeModel):
    id_Role = models.BigAutoField(primary_key=True)
    Libelle = models.CharField(max_length=20)


class Groupe(TimeModel):
    id_Groupe = models.BigAutoField(primary_key=True)
    Nom = models.CharField(max_length=50)


class Commentaire(TimeModel):
    id_Com = models.BigAutoField(primary_key=True)
    id_Ressources = models.ForeignKey(Ressources, on_delete=models.CASCADE)
    Auteur = models.CharField(max_length=100)
    Commentaire = models.TextField()


class Reponse(TimeModel):
    id_Reponse = models.BigAutoField(primary_key=True)
    id_Commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE)
    Auteur = models.CharField(max_length=100)
    Reponse = models.TextField()


# Test
class Post(TimeModel):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
