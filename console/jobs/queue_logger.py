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
    user=None,
    method="",
    event="",
    input="",
    output=""
):
    data = {
        'user':user,
        'method':method,
        'event':event,
        'input':input,
        'output':output
    }
    
    data_save = LoggerSerializer(data=data)
    if not data_save.is_valid():
        print(data_save.errors)
    data_save.save()