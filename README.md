# Miniblog CIN

Miniblog CIN es un proyecto de blog minimalista desarrollado con Django. Este proyecto incluye funcionalidades básicas como la creación, lectura, actualización y eliminación de publicaciones, así como la gestión de usuarios y reseñas de productos.

## Requisitos

- Python 3.10 o superior
- Django 5.0.4
- Virtualenv (recomendado)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd miniblog_cin
Crea y activa un entorno virtual:

bash
Copiar código
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Realiza las migraciones de la base de datos:

bash
Copiar código
python manage.py migrate
Crea un superusuario para acceder al panel de administración:

bash
Copiar código
python manage.py createsuperuser
Ejecuta el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Accede a la aplicación en tu navegador en http://127.0.0.1:8000/.

Estructura del Proyecto
miniblog_cin/ - Directorio principal del proyecto.
product/ - Aplicación que gestiona los productos y reseñas.
users/ - Aplicación que gestiona la autenticación y los perfiles de usuarios.
templates/ - Directorio de plantillas HTML.
static/ - Archivos estáticos (CSS, JavaScript, imágenes).
Funcionalidades
Usuarios
Registro y autenticación de usuarios.
Gestión de perfiles de usuario.
Productos y Reseñas
Listado de productos.
Creación, lectura, actualización y eliminación de reseñas de productos.
Uso
Gestión de Productos
Accede al panel de administración en http://127.0.0.1:8000/admin/.
Añade, edita o elimina productos desde el panel de administración.
Gestión de Reseñas
Inicia sesión en la aplicación.
Accede a la sección de productos.
Añade, edita o elimina reseñas de productos.
