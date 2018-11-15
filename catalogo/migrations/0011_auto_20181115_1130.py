# Generated by Django 2.1.2 on 2018-11-15 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_auto_20181115_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicicleta',
            name='aro',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='catalogo',
            name='bicicleta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Bicicleta'),
        ),
    ]
