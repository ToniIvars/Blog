from django.db import models

# Create your models here.

class entradas_blog(models.Model):
    creador=models.CharField(max_length=30)
    titulo=models.CharField(max_length=80)
    cuerpo=models.TextField(max_length=20000)
    slug=models.SlugField(max_length=80)

    objects=models.Manager()

    def __str__(self):
        return self.creador


class comentarios(models.Model):
    entrada=models.CharField(max_length=80)
    autor=models.CharField(max_length=30)
    cuerpo=models.TextField(max_length=5000)

    objects=models.Manager()

    def __str__(self):
        return self.entrada