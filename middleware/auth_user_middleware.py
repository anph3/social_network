from django.middleware.security import *
from django.conf import settings
from configs.variable_response import *
from configs.variable_system import *
from django.core.cache import cache
from helpers.response import *
from api_app import urls
from django.urls import resolve

class AuthUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = resolve(request.path_info).url_name
        
        list_url = []
        for item in GROUP_URL:
            list_url += self.get_list_url(item)
        
        if current_url in list_url:
            return self.get_response(request)
        header_token = request.headers.get("Authorization")
        
        if header_token is None:
            return json_response(status=STATUS['NOT_LOGIN'], message=ERROR['not_login'])
        
        header_token = header_token.replace(TOKEN['type'], '')
        token = cache.get(header_token)
        if token is None:
            return json_response(status=STATUS['TOKEN_EXPIRED'], message=ERROR['access_token'])
        
        # redis_data = cache.get(token) 
        return self.get_response(request)
    
    def get_list_url(self, value):
        list_url = []
        for item in urls.all_url[value]:
            str_url = str(item.name)
            list_url.append(str_url)
        return list_url