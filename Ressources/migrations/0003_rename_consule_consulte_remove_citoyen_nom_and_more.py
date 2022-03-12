# Generated by Django 4.0.3 on 2022-03-07 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ressources', '0002_alter_ressources_stockage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consule',
            new_name='Consulte',
        ),
        migrations.RemoveField(
            model_name='citoyen',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='citoyen',
            name='prenom',
        ),
        migrations.AddField(
            model_name='citoyen',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]