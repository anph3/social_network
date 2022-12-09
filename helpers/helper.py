from django.core.cache import cache
from configs.variable_system import *

def get_user_info(request):
    data = request.headers.get("Authorization").replace(TOKEN['type'], '')
    a = cache.get(data)
    r = cache.get(a)
    return r