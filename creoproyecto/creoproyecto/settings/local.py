from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project_db',
        'USER': 'test1',
        'PASSWORD': 'test1',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}