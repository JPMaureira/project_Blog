# # models.py
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
# from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

class UsuarioPersonalizadoManager(BaseUserManager):
    def create_user(self, email, password=None, nombre=None, **extra_fields):
        if not email:
            raise ValueError('El campo Email debe ser establecido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, nombre=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, nombre, **extra_fields)


class UsuarioPersonalizado(AbstractUser):
    nombre = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=20, blank=True)
    objects = UsuarioPersonalizadoManager()
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='custom_user_permissions')


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='page_images/')
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE )
    image = models.ImageField(upload_to="avatares", null= True, blank=True)



