# Generated by Django 2.1.2 on 2018-11-15 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20181115_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogo',
            name='bicicleta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Bicicleta'),
        ),
    ]
