# Generated by Django 4.2.6 on 2023-11-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_compras_dir_envio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='dir_envio',
            field=models.CharField(default='Pendiente', max_length=1000),
        ),
        migrations.AlterField(
            model_name='compras',
            name='provincia_envio',
            field=models.CharField(default='Pendiente', max_length=100),
        ),
    ]
