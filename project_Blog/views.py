from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.template import Template, Context
from .models import UsuarioPersonalizado
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render, redirect
from .forms import UserRegisterForm,PageForm
from .models import Page
from .forms import BuscarEventoForm
from django.contrib.auth.models import User
from .forms import UserEditForm

from django.contrib.auth.decorators import login_required


from django.contrib import messages

# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"panel.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect('panel')  # Redirige a la vista panel
            else:
                return render(request, "home.html", {"mensaje": "Datos incorrectos"})
        else:
            return render(request, "home.html", {"mensaje": "Formulario erroneo"})

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required  # Este decorador asegura que solo los usuarios autenticados puedan acceder a la vista
def panel(request):
   
    usuario = request.user
    context = {"usuario": usuario}
    return render(request, "panel.html", context)

def home(request):
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return redirect('home.html')


def about(request):
    return render(request, 'about.html')

def perfiles(request):
    usuarios = User.objects.all()
    return render(request, 'perfiles.html', {'usuarios': usuarios})

def pages(request):
    return render(request, 'pages.html')

@login_required
def create_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.save()
            messages.success(request, 'Page created successfully!')
            return redirect('page_creada')
    else:
        form = PageForm()
    return render(request, 'create_page.html', {'form': form})

@login_required
def page_creada(request):
     
    messages_to_show = request.session.get('messages_to_show', [])

    request.session['messages_to_show'] = []
    
    pages = Page.objects.all()

    form_buscar = BuscarEventoForm(request.GET)
    if form_buscar.is_valid():
        busqueda = form_buscar.cleaned_data['busqueda']
        pages = pages.filter(Q(title__icontains=busqueda) | Q(author__icontains=busqueda))

    return render(request, 'page_creada.html', {'pages': pages, 'messages_to_show': messages_to_show, 'form_buscar': form_buscar})


def eliminar_page(request, page_id):
    page = Page.objects.get(pk=page_id)
    page.delete()
    messages.success(request, 'Page eliminado exitosamente.')
    return redirect('page_creada')


def editar_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)

    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)

        if form.is_valid():
            form.save()
            messages.success(request, 'Page editado exitosamente.')
            return redirect('page_creada')
    else:
        form = PageForm(instance=page)

    return render(request, 'editar_page.html', {'form': form, 'page_id': page_id})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('panel')  # O la URL que desees después de la edición exitosa
    else:
        form = UserEditForm(instance=request.user)

    return render(request, "edit_profile.html", {"form": form})