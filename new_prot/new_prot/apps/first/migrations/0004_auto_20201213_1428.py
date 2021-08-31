# Generated by Django 3.0.8 on 2020-12-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_auto_20201213_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicacion',
            name='t_ubi',
            field=models.CharField(choices=[('plaza', 'plaza'), ('comida', 'comida'), ('comercial', 'comercial'), ('alojamiento', 'alojamiento'), ('educativo', 'educativo'), ('medico', 'medico'), ('religioso', 'religioso')], max_length=25, verbose_name='tipo de lugar'),
        ),
    ]