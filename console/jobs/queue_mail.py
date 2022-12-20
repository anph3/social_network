from celery import shared_task
from configs import variable_system as vs
from api_app.serializers.mail_serializer import *
from helpers.response import *
from social_network.celery import app

# celery -A social_network beat -l INFO
# celery -A social_network worker -l INFO

@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs=vs.CELERY_QUEUE['retry_task']
)
def add_mail(data):
    mail_save = MailSerializer(data=data)
    if mail_save.is_valid():
        mail_save.save()
    
@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs=vs.CELERY_QUEUE['retry_task']
)
def edit_mail(id, data):
    queryset = TemplateMail.objects.get(id=id)
    data_save = MailSerializer(queryset, data=data, partial=True)
    if data_save.is_valid():
        data_save.save()
    
@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs=vs.CELERY_QUEUE['retry_task']
)
def delete_mail(id, data=None):
    queryset = TemplateMail.objects.get(id=id)
    queryset.deleted_at = data
    queryset.save()
    
@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs=vs.CELERY_QUEUE['retry_task']
)
def drop_mail(id):
    queryset = TemplateMail.objects.get(id=id)
    queryset.delete()