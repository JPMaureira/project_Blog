# Blog en Django

Este es un blog simple creado con Django y Python, siguiendo el patrón Modelo Vista Controlador (MVC). Permite la creación, edición, eliminación y listado de páginas que se publican en el blog. La base de datos está implementada con SQLite.

## Configuración del entorno

Asegúrate de tener Python y Django instalados en tu entorno de desarrollo. Puedes instalar las dependencias con el siguiente comando:

```bash
pip install -r requirements.txt


# Configuración de la base de datos

El proyecto utiliza SQLite como base de datos por defecto. Puedes configurar la base de datos y aplicar las migraciones con los siguientes comandos:

1. **Configuración inicial de la base de datos:**

   Abre el archivo `settings.py` en la carpeta `blog_project` y asegúrate de que la configuración de la base de datos esté como sigue:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / "db.sqlite3",
       }
   }
# Aplicar las migraciones iniciales:
python manage.py makemigrations
python manage.py migrate

# Crear un superusuario (opcional):

python manage.py createsuperuser

# Iniciar el servidor de desarrollo:

python manage.py runserver

# Manual de Usuario
¡Bienvenido al Sistema de Blog!

#Registro en el Sistema:

Para ingresar al emocionante mundo del Blog, primero, debes registrarte.
Una vez que completes el proceso de registro, serás redirigido a una página que confirma tu éxito como usuario registrado.

¡Importante! Asegúrate de recordar tu nombre de usuario, ya que será tu llave de acceso en futuras sesiones.

Funcionalidades Principales:
Creación y Gestión de Páginas:

Explora la opción de "Crear Página" para compartir tus pensamientos y experiencias.Sube imágenes para personalizar tu contenido.

Disfruta de la flexibilidad de editar o eliminar tus propias páginas según tus necesidades.
Exploración de Contenido:

Accede a la opción de búsqueda para descubrir las fascinantes páginas de otros usuarios.

Encuentra inspiración y conéctate con la comunidad.
Búsqueda de Usuarios:

Utiliza la función de búsqueda para localizar a otros usuarios registrados.
Amplía tu red y descubre nuevas perspectivas.

Edición de Datos de Usuario:

Mantén tus detalles de usuario actualizados.
Explora la opción de "Editar Perfil" para reflejar los cambios que desees.
¡Disfruta de tu experiencia en el Sistema de Blog y comparte tus ideas con el mundo!


