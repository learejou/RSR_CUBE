from django.db import models
# Create your models here.


class Citoyen(models.Model):
    id_Citoyen = models.BigAutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Date_naissance = models.DateField('Date de naissance')
    Mail = models.EmailField(max_length=75)
    Actif = models.BooleanField()


class Ressources(models.Models):
    id_Ressources = models.BigAutoField(primary_key=True)
    Titre = models.CharField(max_length=100)
    Date_crea = models.DateField('Date de création')
    Auteur = models.CharField(max_length=100)
    Stockage = models.CharField(max_length=500)
    Valide = models.BooleanField()


class Consule(models.Models):
    id_Citoyen = models.ForeignKey(Citoyen, on_delete=models.CASCADE)
    id_Ressources = models.ForeignKey(Ressources, on_delete=models.CASCADE)
    Favoris = models.BooleanField()
    Exploite = models.BooleanField()
    Sauvegarde = models.BooleanField()


class Role(models.Models):
    id_Role = models.BigAutoField(primary_key=True)
    Libelle = models.CharField(max_length=20)


class Groupe(models.Models):
    id_Groupe = models.BigAutoField(primary_key=True)
    Nom = models.CharField(max_length=50)


class Commentaire(models.Models):
    id_Com = models.BigAutoField(primary_key=True)
    id_Ressources = models.ForeignKey(Ressources, on_delete=models.CASCADE)
    Auteur = models.CharField(max_length=100)
    Date = models.DateField('Date de publication')
    Commentaire = models.CharField(max_length=250)


class Reponse(models.Models):
    id_Reponse = models.BigAutoField(primary_key=True)
    id_Commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE)
    Auteur = models.CharField(max_length=100)
    Date = models.DateField('Date de réponse')
    Reponse = models.CharField(max_length=250)

