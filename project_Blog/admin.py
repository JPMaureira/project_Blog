from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import  UsuarioPersonalizado,Page,Avatar


admin.site.register(UsuarioPersonalizado)
admin.site.register(Page)
admin.site.register(Avatar)



AUTH_USER_MODEL = 'project_Blog.UsuarioPersonalizado'