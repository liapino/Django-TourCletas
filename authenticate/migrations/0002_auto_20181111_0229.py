# Generated by Django 2.0.4 on 2018-11-11 02:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='User',
        ),
    ]
