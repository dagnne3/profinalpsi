from django.contrib import admin  # Importa el módulo de administración de Django
from .models import Practica  # Importa el modelo Practica para registrarlo

# Decorador para registrar el modelo Practica con la configuración de PracticaAdmin
@admin.register(Practica)
class PracticaAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "is_admin", "password")  # Define qué columnas se muestran en la lista del panel de admin
    list_editable = ("is_admin",) # Allow editing directly in list
    search_fields = ("username",)                  # Habilita una barra de búsqueda para filtrar por username
    list_filter = ("username",)                    # Agrega un filtro lateral para filtrar por username