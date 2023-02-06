from decouple import config

DEBUG = True


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'middleware.auth_user_middleware.AuthUserMiddleware',
]

DEFAULT_THROTTLE_CLASSES = [
    'middleware.throttling.ExtendedRateThrottle'
]

TEMPLATES_DIRS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'my_project',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1'
        # redis://username:password@127.0.0.1:6379
    }
}

SESSION_CACHE_ALIAS = 'default'

STATIC_URL = 'static/'