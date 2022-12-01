from django.middleware.security import *
from django.conf import settings
from configs.variable_response import *
from configs.variable_system import *
from django.core.cache import cache
from helpers.response import *

class AuthUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path in MIDDLEWARE_NOT_APPLY:
            return self.get_response(request)
        headerToken = request.headers.get("Authorization")
        headerToken = headerToken.replace(TOKEN['type'], '')
        
        if headerToken is None:
            return json_response(status=STATUS['NOT_LOGIN'], message=ERROR['not_login'])
        
        token = cache.get(headerToken)
        if token is None:
            return json_response(status=STATUS['NOT_PERMISSION'], message=ERROR['refresh_token'])
        
        # redis_data = cache.get(token)
        return self.get_response(request)