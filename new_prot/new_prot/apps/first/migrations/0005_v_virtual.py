# Generated by Django 3.0.8 on 2021-01-27 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_auto_20201213_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='v_virtual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(help_text='ingrese la url', max_length=255, verbose_name='url')),
                ('ubi', models.OneToOneField(help_text='a que lugar pertenecen estos datos?', on_delete=django.db.models.deletion.CASCADE, to='first.ubicacion')),
            ],
        ),
    ]
