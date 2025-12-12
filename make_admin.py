import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nuestroproyecto.settings')
django.setup()

from vistas.models import Practica

username = input("Enter the username to make admin: ")
try:
    user = Practica.objects.get(username=username)
    user.is_admin = True
    user.save()
    print(f"Success! '{username}' is now an Admin.")
except Practica.DoesNotExist:
    print(f"Error: User '{username}' not found.")
