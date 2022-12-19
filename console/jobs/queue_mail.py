from celery import shared_task
from configs.variable_system import CELERY_QUEUE
from api_app.serializers.mail_serializer import *
from helpers.response import *
from social_network.celery import app

@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs=CELERY_QUEUE['retry_task']
)
def add_mail(data):
    # value.save()
    mail_save = MailSerializer(data=data)
    if not mail_save.is_valid():
        return mail_save.errors
    mail_save.save()
    
@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs=CELERY_QUEUE['retry_task']
)
def edit_mail(id, data):
    # value.save()
    queryset = TemplateMail.objects.get(id=id)
    data_save = MailSerializer(queryset, data=data, partial=True)
    if not data_save.is_valid():
        return validate_error(data_save.errors)
    data_save.save()