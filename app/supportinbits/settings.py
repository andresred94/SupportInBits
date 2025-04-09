"""
Django settings for supportinbits project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i2791=hxsj@57o_q*#wdlp@*6b69y6c1c58)wo8##f7(mu%41f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '63.176.70.247',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'page.apps.PageConfig',
    'user.apps.UserConfig',
    'bootstrap5',
    'cookie_consent',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Añade esta línea

]

ROOT_URLCONF = 'supportinbits.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'supportinbits.context_processors.breadcrumbs',
            ],
        },
    },
]

WSGI_APPLICATION = 'supportinbits.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {  # MongoDB para posts del blog
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'supportinbits',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',  # O la IP del servidor si es remoto
        'PORT': '3306',       # Puerto de MySQL (por defecto: 3306)
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # Modo estricto de MySQL
        }
    },
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'staticFiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticFiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'supportinbits/static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cookies

# Configuración de cookies
COOKIE_CONSENT_NAME = "cookie_consent"
COOKIE_CONSENT_OPTIONS = {
    "necessary": {
        "title": "Cookies necesarias",
        "description": "Cookies esenciales para el funcionamiento del sitio",
        "required": True,
    },
    "analytics": {
        "title": "Cookies analíticas",
        "description": "Cookies para análisis de uso del sitio",
        "required": False,
    }
}

TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 800,
    'menubar': True,
    'plugins': 'a11ychecker,advlist,autolink,lists,link,image,charmap,print,preview,anchor,'
               'searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,'
               'code,help,wordcount',
    'toolbar': 'undo redo | formatselect | bold italic backcolor | '
               'alignleft aligncenter alignright alignjustify | '
               'bullist numlist outdent indent | removeformat | help | a11ycheck',
    'a11ychecker_level': 'aaa',  # Nivel de accesibilidad (opcional)
}