# Generated by Django 4.0.3 on 2022-03-07 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ressources', '0003_rename_consule_consulte_remove_citoyen_nom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citoyen',
            name='mail',
        ),
    ]