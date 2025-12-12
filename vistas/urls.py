from django.urls import path
from . import views

urlpatterns = [
    # --- Autenticación y Acceso ---
    path('', views.login_view, name='login'), # Ruta raíz: lleva al login
    path('login/', views.login_view, name='login_alias'), # Alias para login
    path('login-admin/', views.login_admin_view, name='login_admin'), # Login exclusivo admin
    path('logout/', views.logout_view, name='logout'), # Cerrar sesión
    path('registro/', views.formulario, name='registro'), # Crear cuenta nueva

    # --- Panel de Control (Dashboard) ---
    path('home/', views.home_view, name='home'), # Inicio para usuarios normales
    path('dashboard/', views.dashboard, name='dashboard'), # Inicio para administradores
    
    # --- Gestión de Tours ---
    path('tours/', views.tours_view, name='tours'), # Ver lista de tours
    path('tours/crear/', views.crear_tour, name='crear_tour'), # Formulario nuevo tour
    path('tours/editar/<int:pk>/', views.editar_tour, name='editar_tour'), # Editar tour existente (usa ID)
    path('tours/eliminar/<int:pk>/', views.eliminar_tour, name='eliminar_tour'), # Eliminar tour (usa ID)

    # --- Gestión de Usuarios y Configuración ---
    path('usuarios/', views.user_register, name='user_register'), # Lista de usuarios (Admin)
    path('usuario/editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'), # Editar otro usuario
    path('configuracion/', views.configuracion_view, name='configuracion'), # Ajustes del sistema
    path('perfil/', views.perfil_view, name='perfil'), # Editar mi propio perfil
    
    # --- Vistas Simples / Legacy ---
    path('saludo/', views.saludo, name='saludo'),
    path('despedida/', views.despedida, name='despedida'),
    path('anime/', views.anime, name='anime'),
    path('plantilla/', views.mundo, name='mundo'),
]
