from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'huseyinkarabas.pythonanywhere.com',
]

INSTALLED_APPS += [
]

MIDDLEWARE += [
]

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

'''
    DEBUG: Hata ayiklama amaçli düşük seviyeli sistem bilgisi
    INFO: Genel sistem bilgisi
    WARNING: Küçük çapli hatalarin bilgisi
    ERROR: Büyük çapli hatalarin bilgisi
    CRITICAL: Kritik hatallarin bilgisi
'''

CORS_ALLOWED_ORIGINS = [
    "https://blog-client-ehkarabas.netlify.app",
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

LOGGING = {
    "version": 1,
 
    "disable_existing_loggers": True,
 
    "formatters": {
        'verbose': {
            'format': 'PRODLOG --{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
 
    "handlers": {
        'file': {
            'class': 'logging.FileHandler',
            "formatter": "verbose",
            'filename': './debug.log',
            'level': 'WARNING',
        },
    },
 
    "loggers": {
        "django": {
            "handlers": ['file'],
 
            "level": config("DJANGO_LOG_LEVEL", "WARNING"),
            'propagate': True,
 
        },
    },
}
