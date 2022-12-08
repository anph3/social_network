from decouple import config

ALLOWED_HOSTS = ['*']

DEBUG = True

ROOT_URLCONF = 'api_app.urls'

DATE_FORMAT = '%d-%m-%Y'

DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'

DATE_INPUT_FORMATS = [
    '%d/%m/%Y',
    '%Y-%m-%d',
    '%d-%m-%Y',
    '%Y/%m/%d'
]

DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d %H:%M:%S',
    '%Y/%m/%d %H:%M:%S',
    '%d-%m-%Y %H:%M:%S',
    '%d/%m/%Y %H:%M:%S'
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'middleware.auth_user_middleware.AuthUserMiddleware',
]

DEFAULT_THROTTLE_CLASSES = [
    'middleware.throttling.ExtendedRateThrottle'
]

DEFAULT_THROTTLE_USER = '1/3s'

TEMPLATES_DIRS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'social_network',
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

REST_FRAMEWORK = {
    'DATE_FORMAT': DATE_FORMAT,
    'DATETIME_FORMAT': DATETIME_FORMAT,
    'DATE_INPUT_FORMATS': DATE_INPUT_FORMATS,
    'DATETIME_INPUT_FORMATS': DATETIME_INPUT_FORMATS,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DEFAULT_THROTTLE_CLASSES': DEFAULT_THROTTLE_CLASSES,
    'DEFAULT_THROTTLE_RATES': {
        'user': DEFAULT_THROTTLE_USER
    },

}