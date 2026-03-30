from django.urls import path
from . import views

urlpatterns = [
    #Urls salas
    path("", views.inicio, name="inicio"),
    path("salas/",views.salas,name="salas"),
    path("salaFormulario",views.salaFormulario,name="salaFormulario"),
    path("buscarSala/",views.buscarSala,name="buscarSala"),
    #Urls Usuarios
    path("usuarios/",views.usuarios,name="usuarios"),
    path("usuarioFormulario",views.usuarioFormulario,name="usuarioFormulario"),
    path("buscarUsuario/",views.buscarUsuario,name="buscarUsuario"),
    #Urls Peliculas
    path("peliculasFormulario",views.peliculasFormulario,name="peliculasFormulario"),
    path("buscarPelicula/",views.buscarPeliculas,name="buscarPeliculas"),
    path("peliculas/",views.PeliculaList.as_view(),name="peliculas"), #Vista basada en clase
    path("PeliculaCrear/",views.PeliculaCrear.as_view(),name="PeliculaCrear"), #Vista basada en clase
    path("PeliculaDetalle/<int:pk> ",views.PeliculaDetalle.as_view(),name="PeliculaDetalle"), #Vista basada en clase
    path("PeliculaEditar/<int:pk> ", views.PeliculaEditar.as_view(),name="PeliculaEditar"), #Vista basada en clase
    path("PeliculaDelete/<int:pk>",views.PeliculaEliminar.as_view(),name="PeliculaDelete") #Vista basada en clase
]