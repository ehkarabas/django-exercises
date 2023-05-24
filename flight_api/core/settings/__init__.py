# from .base import *
# from .development import *
# from .production import *

from decouple import config

ENVIRONMENT = config('ENV')
if ENVIRONMENT == 'development':
    from .development import *
else:
    from .production import *
