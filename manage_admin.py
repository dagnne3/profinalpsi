import os
import django
import sys

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nuestroproyecto.settings')
django.setup()

from vistas.models import Practica

def list_admins():
    print("\n--- Administradores Actuales ---")
    admins = Practica.objects.filter(is_admin=True)
    if admins.exists():
        for admin in admins:
            print(f"- {admin.username}")
    else:
        print("No se encontraron administradores.")
    print("------------------------------\n")

def main():
    while True:
        list_admins()
        print("¿Qué deseas hacer?")
        print("1. Promover un usuario a Administrador")
        print("2. Quitar permisos de Administrador")
        print("3. Salir")
        
        choice = input("\nIngresa tu opción (1-3): ")
        
        if choice == '3':
            break
            
        username = input("Ingresa el nombre de usuario: ")
        
        try:
            user = Practica.objects.get(username=username)
            
            if choice == '1':
                user.is_admin = True
                user.save()
                print(f"¡ÉXITO: '{username}' ahora es Administrador!")
            elif choice == '2':
                user.is_admin = False
                user.save()
                print(f"¡ÉXITO: '{username}' ya no es Administrador.")
            
        except Practica.DoesNotExist:
            print(f"ERROR: El usuario '{username}' no existe.")
        except Exception as e:
            print(f"Error: {e}")
            
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
