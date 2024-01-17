from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import  UsuarioPersonalizado,Page


admin.site.register(UsuarioPersonalizado)
admin.site.register(Page)



AUTH_USER_MODEL = 'project_Blog.UsuarioPersonalizado'