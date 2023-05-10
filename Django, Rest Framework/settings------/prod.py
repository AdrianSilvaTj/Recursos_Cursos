from .base import *

# CONFIGURACION PARA TRABAJAR EN RENDER

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "inmueblesdb_77iy",
        'USER': "adrian",
        'PASSWORD': "2T6ABL88ZoYJNw9YrjPH21LJvpiXc3kI",
        'HOST': "postgres://adrian:2T6ABL88ZoYJNw9YrjPH21LJvpiXc3kI@dpg-chdc758rddlf3vv9gj2g-a/inmueblesdb_77iy",
        'PORT': '5432'
    }
}
