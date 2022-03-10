# Generated by Django 4.0.2 on 2022-03-10 16:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0004_alter_commentaire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 10, 17, 1, 43, 864072), verbose_name='Date du commentaire'),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='id_ressources',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSR.ressources'),
        ),
        migrations.AlterField(
            model_name='reponse',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 10, 17, 1, 43, 865072), verbose_name='Date de la reponse'),
        ),
    ]
