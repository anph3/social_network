from celery import shared_task
from configs import variable_system as vs
from api_app.serializers.logger_serializer import *
from social_network.celery import app

# celery -A social_network beat -l INFO
# celery -A social_network worker -l INFO

@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs=vs.CELERY_QUEUE['retry_task']
)
def add_logger(
    headers = None,
    body = '',
    method = '',
    path = '',
    output = ''
): 
    id = None
    if headers is not None:
        headers = headers.replace(vs.TOKEN['type'], '')
        a_token = cache.get(headers)
        r_token = cache.get(a_token)
        id = r_token['id']
        
    data = {
        'user':id,
        'method':str(method),
        'event':str(path),
        'input':str(body),
        'output':str(output)
    }
    
    data_save = LoggerSerializer(data=data)
    if not data_save.is_valid():
        print(data_save.errors)
    data_save.save()