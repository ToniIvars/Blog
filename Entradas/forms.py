from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core import validators

class FormNuevaEntrada(forms.Form):
    creador=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':28, 'readonly':True}), initial='')
    titulo=forms.CharField(max_length=80, widget=forms.TextInput(attrs={'size':80, 'placeholder':'80 caracteres'}))
    cuerpo_texto=forms.CharField(widget=forms.Textarea(attrs={'rows':28, 'cols':180, 'placeholder':'20.000 caracteres'}), max_length=20000)

class FormEditarEntrada(forms.Form):
    creador=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':28, 'readonly':True}), initial='')
    titulo=forms.CharField(max_length=80, widget=forms.TextInput(attrs={'size':80}))
    cuerpo_texto=forms.CharField(widget=forms.Textarea(attrs={'rows':28, 'cols':180}), max_length=20000)

class FormContacto(forms.Form):
    email=forms.EmailField(widget=forms.TextInput(attrs={'size':28, 'readonly':True}), initial='')
    asunto=forms.CharField(widget=forms.TextInput(attrs={'size':80}))
    mensaje=forms.CharField(widget=forms.Textarea(attrs={'rows':30, 'cols':160}))

class SignupForm(forms.Form):
    username=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30, 'placeholder':'Nombre de usuario', 'class':'user-field'}), label='')
    password=forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={'size':30, 'placeholder':'Escribe la contraseña', 'class':'user-field'}), validators=[validate_password], label='')
    password2=forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={'size':30, 'placeholder':'Confirma la contraseña', 'class':'user-field'}), label='')
    email=forms.EmailField(max_length=40, widget=forms.TextInput(attrs={'size':30, 'placeholder':'Email', 'class':'user-field'}), label='')

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30, 'placeholder':'Usuario', 'class':'user-field'}), label='')
    password=forms.CharField(max_length=12, widget=forms.PasswordInput(attrs={'size':30, 'placeholder':'Contraseña', 'class':'user-field'}), label='')

class FormEditarPerfil(forms.Form):
    username=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), label='Nombre de usuario')
    first_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), label='Nombre')
    last_name=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':30}), label='Apellidos')
    email=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'size':30}))