# Generated by Django 4.0.3 on 2022-03-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ressources', '0006_alter_ressources_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='ressources',
            name='refus',
            field=models.BooleanField(default=False),
        ),
    ]
