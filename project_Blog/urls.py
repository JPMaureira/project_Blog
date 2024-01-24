"""
URL configuration for project_Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import  home, login_request, register, panel,about,create_page,pages,page_creada,eliminar_page,editar_page,perfiles,edit_profile
from django.contrib.auth.views import LogoutView
from django.conf import settings

from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('', home),  
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('panel/', panel, name='panel'),
    path('perfiles/', perfiles, name='perfiles'),
    path('about/', about, name='about'),
    path('create_page/', create_page, name='create_page'),
    path('pages/', pages, name='pages'),
    path('page_creada/', page_creada, name='page_creada'),
    path('eliminar_page/<int:page_id>/', eliminar_page, name='eliminar_page'),
    path('editar_page/<int:page_id>/', editar_page, name='editar_page'),
    path('edit_profile/', edit_profile, name='edit_profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
