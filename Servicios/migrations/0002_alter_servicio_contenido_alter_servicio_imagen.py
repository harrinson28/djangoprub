# Generated by Django 5.1.2 on 2024-11-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]
