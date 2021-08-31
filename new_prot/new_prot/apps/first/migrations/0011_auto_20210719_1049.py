# Generated by Django 3.0.8 on 2021-07-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0010_auto_20210719_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicacion',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='t_ubi',
            field=models.CharField(choices=[('plaza', 'plaza'), ('comida', 'comida'), ('comercial', 'comercial'), ('alojamiento', 'alojamiento'), ('educativo', 'educativo'), ('medico', 'medico'), ('religioso', 'religioso'), ('atractivo', 'atractivo')], max_length=45, verbose_name='tipo de lugar'),
        ),
    ]
