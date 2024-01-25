from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import UsuarioPersonalizado
from django.contrib.auth.models import User
from .models import Page
from django.contrib.auth.forms import UserChangeForm


class UserRegisterForm(UserCreationForm):
    email     = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

  
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'image','author']

class BuscarEventoForm(forms.Form):
    busqueda = forms.CharField(label='Buscar evento', max_length=100)


class UserEditForm(UserChangeForm):
    password = None  # Elimina el campo de contraseña por defecto
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_password(self):
        # Limpia el campo de contraseña para evitar cambios no deseados
        return None
