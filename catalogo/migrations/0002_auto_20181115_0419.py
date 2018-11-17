# Generated by Django 2.1.2 on 2018-11-15 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_catalogo', models.CharField(choices=[('MONT', 'Montaña'), ('URB', 'Urbana'), ('RU', 'Ruta'), ('EQUIP', 'Equipamiento')], max_length=50)),
                ('codigo', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_equipamiento', models.CharField(choices=[('RO', 'Rodillera'), ('CO', 'Caso'), ('BT', 'Botiquin'), ('HR', 'Herramientas')], default=None, max_length=100)),
                ('precio_equipamiento', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sede', models.CharField(max_length=20)),
                ('ciudad_sede', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='bicicleta',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='bicicleta',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='bicicleta',
            name='color',
        ),
        migrations.RemoveField(
            model_name='bicicleta',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='bicicleta',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='bicicleta',
            name='talla',
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='cantidad',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='estado',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='tipo_bicicleta',
            field=models.CharField(choices=[('MONT', 'Montaña'), ('URB', 'Urbana'), ('RU', 'Ruta')], default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='bicicleta',
            name='ubicacion',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='aro',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_bicicletas'),
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='marca',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='precio',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='bicicleta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Bicicleta'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='equipamiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Equipamiento'),
        ),
        migrations.AddField(
            model_name='catalogo',
            name='sede',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Sede'),
        ),
    ]