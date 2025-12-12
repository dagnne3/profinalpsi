from django.db import models

class Practica(models.Model):
    """
    Modelo de Usuario del sistema (nombre legacy 'Practica').
    Se usa para almacenar tanto administradores como usuarios normales.
    Define campos para login (usuario/pass) y datos personales.
    Campos legado/migración se mantienen como null=True para evitar conflictos.
    """
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128) # Nota: En prod usar hashlib o AbstractUser
    imagen_url = models.URLField(max_length=500, blank=True, null=True)
    
    # Nuevos campos para registro completo (alineado con diseño)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    is_admin = models.BooleanField(default=False) # Distingue admins de usuarios

    def __str__(self):
        return self.username

class Tour(models.Model):
    """
    Modelo para los Tours turísticos.
    Separa los items en dos grandes categorías: 'ciudad' y 'lugar'.
    Almacena nombre, imagen, duración y descripción para mostrar en las tarjetas.
    """
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen_url = models.URLField(max_length=500, blank=True, null=True)
    duracion = models.CharField(max_length=50) # Ej: "5 Días"
    categoria = models.CharField(
        max_length=10,
        choices=[('ciudad', 'Ciudad'), ('lugar', 'Lugar')],
        default='ciudad'
    )

    def __str__(self):
        return self.nombre