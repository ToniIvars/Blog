# Generated by Django 3.0.5 on 2020-05-06 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Entradas', '0005_auto_20200506_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradas_blog',
            name='fecha',
        ),
    ]
