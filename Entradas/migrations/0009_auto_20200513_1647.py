# Generated by Django 3.0.5 on 2020-05-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entradas', '0008_auto_20200513_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas_blog',
            name='contra',
            field=models.CharField(max_length=12, verbose_name='contraseña'),
        ),
    ]