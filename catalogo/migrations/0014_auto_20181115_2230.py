# Generated by Django 2.1.2 on 2018-11-15 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0013_auto_20181115_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogo',
            name='bicicleta',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='equipamiento',
        ),
        migrations.RemoveField(
            model_name='catalogo',
            name='sede',
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Catalogo'),
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Catalogo'),
        ),
    ]