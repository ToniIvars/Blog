from django.contrib import admin
from Entradas.models import entradas_blog, comentarios

# Register your models here.

class entradas_admin(admin.ModelAdmin):
    list_display=('titulo', 'creador')
    search_fields=('titulo', 'creador')
    list_filter=('creador',)

class comentarios_admin(admin.ModelAdmin):
    list_display=('entrada', 'autor')
    search_fields=('entrada',)
    list_filter=('entrada', 'autor')

admin.site.register(entradas_blog, entradas_admin)
admin.site.register(comentarios, comentarios_admin)