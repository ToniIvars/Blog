# Generated by Django 3.0.5 on 2020-05-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entradas', '0010_remove_entradas_blog_contra'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.CharField(max_length=80)),
                ('autor', models.CharField(max_length=30)),
                ('comentario', models.TextField(max_length=5000)),
            ],
        ),
    ]
