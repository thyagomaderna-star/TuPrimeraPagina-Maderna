from django.contrib import admin
from .models import Pelicula, Usuario, Sala
# Register your models here.


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display=["nombre","autor","fecha_estreno","genero"]
    list_filter = ["nombre","autor","genero"]
    ordering = ["-fecha_estreno"]

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=["nombre","apellido","email"]
