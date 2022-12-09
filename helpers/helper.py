from django.core.cache import cache
from configs.variable_system import *
import json
import requests

def get_user_info(request):
    data = request.headers.get("Authorization").replace(TOKEN['type'], '')
    a = cache.get(data)
    r = cache.get(a)
    return r

def call_api(**kwargs):
    try:
        host = kwargs.pop("host")
        func = kwargs.pop("func")
        method = kwargs.pop("method")
        data = kwargs.pop("data", None)
        headers = kwargs.pop("headers", {'Content-Type': 'application/json'})
        payload = json.dumps(data)
        response = requests.request(method, host+func, headers=headers, data=payload)
        return response.text
    except:
        None