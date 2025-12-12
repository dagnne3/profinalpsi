from django import forms
from .models import Practica, Tour

class LoginForm(forms.Form):
    """
    Formulario simple para inicio de sesión.
    No está vinculado a un modelo directamente, solo valida los campos de entrada.
    Se usa tanto para admin como para usuarios.
    """
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}))

class RegistroForm(forms.ModelForm):
    """
    Formulario para registrar nuevos usuarios.
    - Incluye campos de contraseña dobles para confirmación.
    - Define widgets CSS (clases) para que se vea bien en el HTML.
    """
    # Campos extra no presentes en el modelo directamente
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'm-bottom', 'id': 'password'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'm-bottom', 'id': 'confirmar_password'}))
    
    class Meta:
        model = Practica
        fields = ['nombre', 'apellido', 'email', 'username', 'imagen_url'] 
        widgets = {
            'username': forms.TextInput(attrs={'class': 'm-bottom', 'id': 'usuario'}),
            'nombre': forms.TextInput(attrs={'class': 'm-bottom'}),
            'apellido': forms.TextInput(attrs={'class': 'm-bottom'}),
            'email': forms.EmailInput(attrs={'class': 'm-bottom'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data

class EditarUsuarioForm(forms.ModelForm):
    """
    Formulario para editar perfil de usuario existente.
    - Permite cambiar foto, datos básicos y opcionalmente la contraseña.
    - Permite asignar o quitar rol de administrador.
    """
    password1 = forms.CharField(label='Nueva Contraseña', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Practica
        fields = ['username', 'imagen_url', 'nombre', 'apellido', 'email', 'is_admin']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_admin': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'is_admin': '¿Es Administrador?',
        }

class TourForm(forms.ModelForm):
    """
    Formulario para crear o editar Tours.
    - Define campos para nombre, descripción, URL de imagen, duración y categoría.
    - Utiliza Textarea para la descripción para dar más espacio.
    """
    class Meta:
        model = Tour
        fields = ['nombre', 'descripcion', 'imagen_url', 'duracion', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duracion': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://ejemplo.com/imagen.jpg'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
