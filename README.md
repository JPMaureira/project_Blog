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

