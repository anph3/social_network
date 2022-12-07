from pytimeparse.timeparse import timeparse
from rest_framework import throttling
from django.urls import resolve

class ExtendedRateThrottle(throttling.UserRateThrottle):
    scope = 'user'
    def parse_rate(self, rate):
        if rate is None:
            return (None, None)
        num, period = rate.split('/')
        num_requests = int(num)
        duration = timeparse(period) 
        return (num_requests, duration)

    def debounce_name(self, request):
        str_name = resolve(request.path_info).url_name
        return str_name
    
    def allow_request(self, request, view):
        if request.method in ['GET']:
            return True
        return super().allow_request(request, view)

    def get_cache_key(self, request, view):
        super().get_cache_key(request, view)
        if request.user and request.user.is_authenticated:
            ident = request.user.pk + self.debounce_name(request)
        else:
            ident = self.get_ident(request) + self.debounce_name(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

# class CustomThrottle(throttling.SimpleRateThrottle):
#     def parse_rate(self, rate):
#         if rate is None:
#             return (None, None)
#         num, period = rate.split(vr_sys.THROTTLING['split'])
#         num_requests = int(num)
#         duration = {vr_sys.THROTTLING['type_time']: vr_sys.THROTTLING['waiting_time']}[period[0]]
#         return (num_requests, duration)
    
#     def allow_request(self, request, view):
#         if request.method in vr_sys.THROTTLING['method']:
#             return True
#         return super().allow_request(request, view)
    
# def custom_exception_handler(exc, context):
#     return response_data(message=exc.detail)
    
# class UserThrottle(CustomThrottle, throttling.UserRateThrottle):
#     rate = vr_sys.THROTTLING['rate'] + vr_sys.THROTTLING['split'] + vr_sys.THROTTLING['type_time']