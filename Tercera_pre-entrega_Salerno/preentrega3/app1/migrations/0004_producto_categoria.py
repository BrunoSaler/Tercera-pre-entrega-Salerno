# Generated by Django 4.2.6 on 2023-11-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_producto_disponible'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.IntegerField(choices=[('1', 'Línea Blanca'), ('2', 'Electrodoméstico'), ('3', 'Informática'), ('4', 'Pendiente')], default=4, max_length=1),
        ),
    ]
