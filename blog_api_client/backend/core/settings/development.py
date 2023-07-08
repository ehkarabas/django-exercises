from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
 
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

AUTH_PASSWORD_VALIDATORS = [
]

INTERNAL_IPS = [
 
    "127.0.0.1",
 
]

'''
    DEBUG: Hata ayiklama amaçli düşük seviyeli sistem bilgisi
    INFO: Genel sistem bilgisi
    WARNING: Küçük çapli hatalarin bilgisi
    ERROR: Büyük çapli hatalarin bilgisi
    CRITICAL: Kritik hatallarin bilgisi
'''

CORS_ALLOW_ALL_ORIGINS = True

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
        "standard": {
            "format": "DEVLOG -- [%(levelname)s] %(asctime)s %(name)s: %(message)s"
        },
        'verbose': {
            'format': 'DEVLOG -- {levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
 
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "INFO",
            "stream": "ext://sys.stdout",
        },
        'file': {
            'class': 'logging.FileHandler',
            "formatter": "verbose",
            'filename': './debug.log',
            'level': 'WARNING',
        },
    },
 
    "loggers": {
        "django": {
            "handlers": ["console", 'file'],
 
            "level": config("DJANGO_LOG_LEVEL", "INFO"),
            'propagate': True,
 
        },
    },
}
