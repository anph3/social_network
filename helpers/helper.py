from django.core.cache import cache
from django.conf import settings
from configs import variable_system as vs
import json
import requests
from django.core.mail import EmailMultiAlternatives

def host(request):
    data = request.META.copy()
    return vs.STR_CURRENT_HOST.format(
        data['wsgi.url_scheme'],
        data['HTTP_HOST']
    )
    
def send_mail(subject='', body='', to=[''], cc=[''], bcc=['']):
    message = EmailMultiAlternatives(
        subject = subject,
        body = '',
        to = to,
        cc = cc,
        bcc = bcc,
        from_email = settings.EMAIL_HOST_USER
    )
    
    message.content_subtype = 'html'
    message.mixed_subtype = 'related'
    
    message.attach_alternative(body,'text/html')
    
    return message.send()
    

def file_to_byte(self, id, type):
        # path file
        path_file = vs.STR_MEDIA_PATH.format(
            vs.MEDIA_ROOT,
            id,
            type
        )
        
        # open file
        file = open(path_file, 'rb')
        
        return file

def get_user_info(request):
    data = request.headers.get('Authorization').replace(vs.TOKEN['type'], '')
    a = cache.get(data)
    r = cache.get(a)
    return r

def call_api(**kwargs):
    try:
        host = kwargs.pop('host')
        func = kwargs.pop('func')
        method = kwargs.pop('method')
        data = kwargs.pop('data', None)
        headers = kwargs.pop('headers', {'Content-Type': 'application/json'})
        payload = json.dumps(data)
        response = requests.request(method, host+func, headers=headers, data=payload)
        return response.text
    except:
        None