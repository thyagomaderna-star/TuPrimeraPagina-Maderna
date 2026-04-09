from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#Formularios de sala

class SalaFormulario(forms.Form):
    nombre= forms.CharField(max_length=2, label="Letra de la sala")
    numero = forms.CharField(label="Numero de la sala")

class BusquedaSalaFormulario(forms.Form):
    nombre= forms.CharField(max_length=2, label="Letra de la sala")
    numero = forms.CharField(label="Numero de la sala")

#Formularios de usuarios

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=50,label="Nombre del usuario")
    apellido = forms.CharField(max_length=50,label="Apellido del usuario")
    email = forms.EmailField(label="Email del usuario")
    password = forms.CharField(max_length=50,label="Contraseña")

class BusquedaUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

#Formulario de Peliculas

class PeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50,label="Nombre de la pelicula")
    autor = forms.CharField(max_length=50, label="Autor")
    fecha_estreno = forms.DateField(label="Fecha de extreno DD/MM/YYYY")
    genero = forms.CharField(max_length=20)

class BusquedaPeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    # Colocar filtros opcionales 
    #autor = forms.CharField(max_length=50)
    #fecha_estreno = forms.DateField()
    #genero = forms.CharField(max_length=20)

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ["username","email","first_name","last_name"]