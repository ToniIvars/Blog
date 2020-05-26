from django.contrib import admin
from django.urls import path
from Entradas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),
    path('resultados/', views.resultados, name='res-busca'),
    path('crear-entrada/', views.crear_entrada, name='crear-entrada'),
    path('editar-entrada/<int:entrada>/', views.editar_entrada, name='editar-entrada'),
    path('eliminar-entrada/<int:entrada>/', views.eliminar_entrada, name='eliminar-entrada'),
    path('entrada/<str:slug>', views.muestra_entrada, name='entrada'),
    path('registro/', views.signup, name='registro'),
    path('iniciar-sesion/', views.login_view, name='iniciar-sesion'),
    path('cerrar-sesion/', views.logout_view, name='cerrar-sesion'),
    path('perfil/<str:profile>/', views.perfil, name='perfil'),
    path('ver-perfil/<str:profile>/', views.ver_perfil, name='ver-perfil'),
    path('editar-perfil/<str:profile>/', views.editar_perfil, name='editar-perfil'),
    path('actualizar-contraseña/<str:profile>/', views.actualizar_contra, name='actualizar-contraseña'),
]