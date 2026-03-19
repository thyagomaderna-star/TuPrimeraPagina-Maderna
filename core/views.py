
from django.shortcuts import render
from .models import Usuario, Pelicula, Sala
from .forms import SalaFormulario, BusquedaSalaFormulario, UsuarioFormulario,BusquedaUsuarioFormulario, BusquedaPeliculaFormulario, PeliculaFormulario

#Paginas principales

def inicio(request):
    return render(request, "core/inicio.html")

def salas(request):
    salas = Sala.objects.all()
    contexto = {"salas": salas}
    return render(request,"core/sala/salas.html",contexto)

def usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {"usuarios": usuarios}
    return render(request,"core/usuarios/usuarios.html",contexto)

def peliculas(request):
    peliculas = Pelicula.objects.all()
    contexto = {"peliculas": peliculas}
    return render(request,"core/peliculas/peliculas.html")

#Formularios 

def salaFormulario(request):
    if request.method == "POST":
        form = SalaFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            numero = form.cleaned_data["numero"]
            sala = Sala(nombre=nombre, numero=numero)
            sala.save()
            return render(request, "core/sala/sala_exito.html")
    else:
        form = SalaFormulario()
    return render(request, "core/sala/sala_formulario.html", {"form": form})

def usuarioFormulario(request):
    if request.method == "POST":
        form = UsuarioFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            email = form.cleaned_data["email"]
            usuario = Usuario(nombre=nombre, apellido=apellido,email=email)
            usuario.save()
            return render(request, "core/usuarios/usuario_exito.html")
    else:
        form = UsuarioFormulario()
    return render(request, "core/usuarios/usuario_formulario.html", {"form": form})

def peliculasFormulario(request):
    if request.method == "POST":
        form = PeliculaFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            autor = form.cleaned_data["autor"]
            fecha_estreno = form.cleaned_data["fecha_estreno"]
            genero = form.cleaned_data["genero"]
            pelicula = Pelicula(nombre = nombre,autor = autor,fecha_estreno = fecha_estreno, genero = genero)
            pelicula.save()
            return render(request,"core/peliculas/pelicula_exito.html")
    else:
        form = PeliculaFormulario()
    return render(request,"core/peliculas/pelicula_formulario.html",{"form": form} )
    
#Busquedas

def buscarSala(request):
    if request.method == "GET":
        form = BusquedaSalaFormulario(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            numero = form.cleaned_data["numero"]
            resultados = Sala.objects.filter(nombre=nombre,numero=numero)
            return render(
                request,
                "core/sala/resultados_busqueda_sala.html",
                {"resultados": resultados, "form": form},
            )
    else:
        form = BusquedaSalaFormulario()
    return render(request, "core/sala/buscar_sala.html", {"form": form})

def buscarUsuario(request):
    if request.method == "GET":
        form = BusquedaUsuarioFormulario(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            email = form.cleaned_data["email"]
            resultados = Usuario.objects.filter(nombre=nombre,apellido=apellido,email=email)
            return render( 
                request, 
                "core/usuarios/resultado_busqueda_usuario.html", 
                {"resultados": resultados , "form": form}
            )
    else:
        form = BusquedaUsuarioFormulario()
    return render(request ,"core/usuarios/buscar_usuario.html",{ "form" : form})


def buscarPeliculas(request):
    if request.method == "GET":
        form = BusquedaPeliculaFormulario(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            autor = form.cleaned_data["autor"]
            fecha_estreno = form.cleaned_data["fecha_estreno"]
            genero = form.cleaned_data["genero"]
            resultados = Pelicula.objects.filter(nombre = nombre,autor = autor,fecha_estreno = fecha_estreno, genero = genero)
            return render(
                request
                ,"core/peliculas/resultado_busqueda_pelicula.html",
                {"resultados": resultados, "form": form})
    else:
        form = PeliculaFormulario()
    return render(request,"core/peliculas/buscar_pelicula.html",{"form": form} )