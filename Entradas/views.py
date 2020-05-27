from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from random import randint

from Entradas.models import entradas_blog, comentarios
from Entradas.forms import FormNuevaEntrada, FormContacto, FormEditarEntrada, SignupForm, LoginForm, FormEditarPerfil

initial_dict_editar={}
initial_dict_crear={}
entrada_a_editar=None
id_entrada=None
username=''

# View 'signup'
codigo_enviado=False
codigo=''
email=''
password=''


def generador_slug(tit):
    slug=tit.lower().replace(' ','-').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
    return slug

def generar_codigo():
    codigo=''
    for i in range(6):
        codigo += str(randint(1,9))

    return codigo

def set_username(request):
    global username
    if username=='':
        username=request.user.username

# Create your views here.

def error_404(request):
    return render(request, '404.html')

def error_500(request):
    return render(request, '500.html')

# @login_required
def inicio(request):
    set_username(request)

    articulos=entradas_blog.objects.order_by('-pk')[:4]
    return render(request, 'inicio.html', {'articulos':articulos})


# @login_required
def muestra_entrada(request, slug):
    set_username(request)

    mostrar=entradas_blog.objects.get(slug=slug)
    com=comentarios.objects.filter(entrada=mostrar.titulo)

    if request.method=='POST':
        autor=request.POST.get('input-autor')
        comentario=request.POST.get('input-comentario')

        nuevo_com=comentarios(entrada=mostrar.titulo, autor=autor, cuerpo=comentario)
        nuevo_com.save()

        messages.success(request, 'El comentario ha sido agregado correctamente.')
        return redirect('entrada', slug)
    
    return render(request, 'muestra-entrada.html', {'entrada_a_mostrar':mostrar, 'comentarios':com})

# @login_required
def resultados(request):
    set_username(request)

    if request.GET['input-ent']:

        articulos=entradas_blog.objects.filter(titulo__icontains=request.GET['input-ent']).order_by('-pk')

        if articulos:
            return render(request, 'buscar-entrada.html', {'entradas':articulos})
        else:
            messages.error(request, 'No se han encontrado entradas.')
            return redirect('inicio')

    else:
        return render(request, 'buscar-entrada.html')


@login_required
def crear_entrada(request):
    global initial_dict_crear
    set_username(request)

    if request.method=='POST':
        nueva_entrada=FormNuevaEntrada(request.POST)

        if nueva_entrada.is_valid():
            info_nueva_entrada=nueva_entrada.cleaned_data
            slug_field=generador_slug(info_nueva_entrada['titulo'])

            try:
                obj=entradas_blog.objects.get(slug=slug_field)

                initial_dict_crear = { 
                    'creador':info_nueva_entrada['creador'],                
                    'cuerpo_texto':info_nueva_entrada['cuerpo_texto'],
                }

                messages.error(request, 'El título de la entrada que intentas crear ya existe.')
                return redirect('crear-entrada')

            except ObjectDoesNotExist:

                ent=entradas_blog(creador=info_nueva_entrada['creador'], titulo=info_nueva_entrada['titulo'], cuerpo=info_nueva_entrada['cuerpo_texto'], slug=slug_field)
                ent.save()

                initial_dict_crear = {}
                return redirect('inicio')

    else:
        initial_dict_crear={'creador':username}
        nueva_entrada=FormNuevaEntrada(initial=initial_dict_crear)

    return render(request, 'crear-entrada.html', {'form':nueva_entrada})

@login_required
def editar_entrada(request, entrada):
    global initial_dict_editar, entrada_a_editar, id_entrada
    set_username(request)

    id_entrada = entrada
    entrada_a_editar=entradas_blog.objects.get(pk=id_entrada)

    initial_dict_editar = { 
        'creador':entrada_a_editar.creador,
        'titulo':entrada_a_editar.titulo,
        'cuerpo_texto':entrada_a_editar.cuerpo,
    }

    if request.method=='POST':
        editar_entrada=FormEditarEntrada(request.POST)

        if editar_entrada.is_valid():
            info_editar_entrada=editar_entrada.cleaned_data

            slug_field=generador_slug(info_editar_entrada['titulo'])

            try:
                obj=entradas_blog.objects.get(slug=slug_field)

                if info_editar_entrada['titulo'] == initial_dict_editar['titulo']:
                    raise ObjectDoesNotExist
                else:
                    messages.error(request, 'El título editado pertenece a otra entrada.')
                    return redirect('editar-entrada')

            except ObjectDoesNotExist:

                entradas_blog.objects.filter(pk=id_entrada).update(creador=info_editar_entrada['creador'], titulo=info_editar_entrada['titulo'], cuerpo=info_editar_entrada['cuerpo_texto'], slug=slug_field)
                    
                messages.success(request, 'Entrada actualizada correctamente.')
                return redirect('perfil', username)
    else:

        editar_entrada=FormEditarEntrada(initial=initial_dict_editar)

    return render(request, 'editar-entrada.html', {'form':editar_entrada})

@login_required
def eliminar_entrada(request, entrada):
    set_username(request)

    if request.GET.get('input-del'):

        entradas_blog.objects.filter(pk=entrada).delete()
                    
        messages.success(request, 'Entrada eliminada correctamente.')
        return redirect('perfil', username)

    elif request.GET.get('nothing'):
        return redirect('perfil', username)

    return render(request, 'eliminar-entrada.html')


def signup(request):
    global username, codigo_enviado, codigo, email, password
    if request.method=='POST':
        registro=SignupForm(request.POST)

        if registro.is_valid():
            info_registro=registro.cleaned_data

            if ' ' in info_registro['username']:
                messages.error(request, 'El nombre de usuario no puede contener espacios.')
                return redirect('registro')  

            else:
                username=info_registro['username']
                password=info_registro['password']
                password2=info_registro['password2']
                email=info_registro['email']

                try:
                    user=User.objects.get_by_natural_key(username)
                    messages.error(request, 'Este usuario ya existe.')
                    return redirect('registro')  

                except ObjectDoesNotExist:
                    if password != password2:
                        messages.error(request, 'Las contraseñas no coinciden.')
                        return redirect('registro')

                    else:
                        user=User.objects.create_user(username, email, password)
                        user.save()
                        login(request, user)

                        messages.success(request, 'El usuario ha sido creado correctamente.')
                        return redirect('inicio')                             
    else:
        registro=SignupForm()

    return render(request, 'signup.html', {'form':registro})

def login_view(request):
    global username

    if request.method=='POST':
        inicio_sesion=LoginForm(request.POST)

        if inicio_sesion.is_valid():
            info_inicio=inicio_sesion.cleaned_data

            username=info_inicio['username']
            password=info_inicio['password']

            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')

            else:
                messages.error(request, 'No ha sido posible iniciar sesión.')
                return redirect('iniciar-sesion')

    else:
        inicio_sesion=LoginForm()

    return render(request, 'login.html', {'form':inicio_sesion})

def logout_view(request):
    logout(request)
    return redirect('iniciar-sesion')


# @login_required
def ver_perfil(request, profile):
    articulos=entradas_blog.objects.filter(creador=profile).order_by('-pk')
    return render(request, 'ver-perfil.html', {'nombre_usuario':profile, 'articulos':articulos})

@login_required
def perfil(request, profile):
    # if profile == username:
    articulos=entradas_blog.objects.filter(creador=profile).order_by('-pk')
    return render(request, 'perfil.html', {'articulos':articulos})

    # else:
    #     messages.error(request, 'El perfil al que intentas acceder no es el tuyo.')
    #     return redirect('inicio')

@login_required
def editar_perfil(request, profile):
    set_username(request)

    if request.method=='POST':
        edicion=FormEditarPerfil(request.POST)

        if edicion.is_valid():
            info_edicion=edicion.cleaned_data

            user=User.objects.get_by_natural_key(username)

            user.username=info_edicion['username']
            user.first_name=info_edicion['first_name']
            user.last_name=info_edicion['last_name']
            user.email=info_edicion['email']
            user.save()

            messages.success(request, 'El perfil ha sido actualizado correctamente.')
            return redirect('editar-perfil', username)

    else:
        obj=User.objects.get_by_natural_key(username)

        initial_dict_contacto={
            'username':obj.username,
            'first_name':obj.first_name,
            'last_name':obj.last_name,
            'email':obj.email,
        }
        edit_perfil=FormEditarPerfil(initial=initial_dict_contacto)

    return render(request, 'editar-perfil.html', {'form':edit_perfil})

@login_required
def actualizar_contra(request, profile):
    set_username(request)

    if request.method=='POST':
        user=User.objects.get_by_natural_key(username)

        contra=request.POST.get('input-contra')
        contra2=request.POST.get('input-contra2')

        if contra == contra2:
            user.set_password(contra)

            messages.success(request, 'La contraseña ha sido actualizado correctamente.')
            return redirect('editar-perfil', username)

        else:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('actualizar-contraseña', username)

    return render(request, 'actualizar-contraseña.html')