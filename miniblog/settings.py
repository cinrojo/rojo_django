

"""
Configuración de Django para el proyecto miniblog.

Generado por 'django-admin startproject' usando Django 4.2.11.

Para más información sobre este archivo, ver
https://docs.djangoproject.com/en/4.2/topics/settings/

Para la lista completa de configuraciones y sus valores, ver
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Construye las rutas dentro del proyecto como BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración rápida para el desarrollo - no apta para producción
# Ver https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# ADVERTENCIA DE SEGURIDAD: mantener la clave secreta usada en producción en secreto
SECRET_KEY = "django-insecure-lm_-3$o_n%#2#zsfnkjszh4@#rb+7@br29ohd0i*#+gggra_3s"

# ADVERTENCIA DE SEGURIDAD: no ejecutar con debug activado en producción
DEBUG = True

# Lista de hosts permitidos para el proyecto (vacía en desarrollo)
ALLOWED_HOSTS = []

# Definición de la aplicación

INSTALLED_APPS = [
    # Aplicaciones de Django por defecto
    "django.contrib.admin",  # Administrador del sitio
    "django.contrib.auth",  # Autenticación y permisos
    "django.contrib.contenttypes",  # Tipos de contenido
    "django.contrib.sessions",  # Gestión de sesiones
    "django.contrib.messages",  # Mensajes de usuario
    "django.contrib.staticfiles",  # Archivos estáticos (CSS, JavaScript, imágenes)

    # Aplicaciones del proyecto
    "product",  # Aplicación para productos
    "home",  # Aplicación para la página principal
    "users"  # Aplicación para la gestión de usuarios
]
 
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",  # Middleware de seguridad
    "django.contrib.sessions.middleware.SessionMiddleware",  # Middleware de sesiones
    "django.middleware.common.CommonMiddleware",  # Middleware común
    "django.middleware.csrf.CsrfViewMiddleware",  # Middleware de protección CSRF
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Middleware de autenticación
    "django.contrib.messages.middleware.MessageMiddleware",  # Middleware de mensajes
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Middleware de protección contra clickjacking
]

# URL raíz del proyecto
ROOT_URLCONF = "miniblog.urls"

# Configuración de plantillas
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",  # Backend para usar plantillas de Django
        "DIRS": [],  # Directorios adicionales donde buscar plantillas
        "APP_DIRS": True,  # Buscar plantillas en las aplicaciones instaladas
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",  # Procesador de contexto para depuración
                "django.template.context_processors.request",  # Procesador de contexto para solicitudes
                "django.contrib.auth.context_processors.auth",  # Procesador de contexto para autenticación
                "django.contrib.messages.context_processors.messages",  # Procesador de contexto para mensajes
                "miniblog.context_processors.context_processors_dolar.dolar_exchange_rates",  # Procesador de contexto personalizado para tasas de cambio del dólar
                "miniblog.context_processors.context_processors_names.all_products_names"  # Procesador de contexto personalizado para nombres de todos los productos
            ],
        },
    },
]

# Aplicación WSGI para el proyecto
WSGI_APPLICATION = "miniblog.wsgi.application"

# Base de datos
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Motor de base de datos a utilizar
        "NAME": BASE_DIR / "db.sqlite3",  # Nombre del archivo de la base de datos
    }
}

# Validación de contraseñas
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # Validador para evitar contraseñas similares a atributos del usuario
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # Validador para establecer una longitud mínima de la contraseña
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # Validador para evitar contraseñas comunes
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # Validador para evitar contraseñas solo numéricas
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "es"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

import os

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')