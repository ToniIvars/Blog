# Generated by Django 3.0.5 on 2020-05-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entradas', '0004_entradas_blog_contra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas_blog',
            name='contra',
            field=models.CharField(default='contraseña', max_length=12),
        ),
        migrations.AlterField(
            model_name='entradas_blog',
            name='creador',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='entradas_blog',
            name='titulo',
            field=models.CharField(max_length=80),
        ),
    ]