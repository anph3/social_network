from django.middleware.security import *
from django.conf import settings
from configs.variable_response import *
from configs.variable_system import *
from django.core.cache import cache
from helpers.response import *
from helpers.url_pattern import *
from api_app import urls

class AuthUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        list_url = get_list_url('url_auth')
                        
        if request.path in list_url:
            return self.get_response(request)
        header_token = request.headers.get("Authorization")
        
        if header_token is None:
            return json_response(status=STATUS['NOT_LOGIN'], message=ERROR['not_login'])
        
        header_token = header_token.replace(TOKEN['type'], '')
        token = cache.get(header_token)
        if token is None:
            return json_response(status=STATUS['NOT_PERMISSION'], message=ERROR['access_token'])
        
        # redis_data = cache.get(token)
        return self.get_response(request)