# Generated by Django 3.0.5 on 2020-05-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entradas_blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creador', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=50)),
                ('cuerpo', models.CharField(max_length=20000)),
                ('fecha', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
