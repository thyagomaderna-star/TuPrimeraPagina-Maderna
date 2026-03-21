from django.contrib import admin
from .models import Pelicula, Usuario, Sala
# Register your models here.

#admin.site.register(Pelicula)
#admin.site.register(Usuario)
#admin.site.register(Sala)

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display=["nombre","autor","fecha_estreno","genero"]
    list_filter = ["nombre","autor","genero"]
    ordering = ["-fecha_estreno"]
