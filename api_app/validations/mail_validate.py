from rest_framework import serializers
from ..models.template_mail import TemplateMail
from configs.variable_response import *
from ..serializers.mail_serializer import *

class MailValidate(serializers.Serializer):
    subject = serializers.CharField()
    body = serializers.CharField()
    to = serializers.ListField()
    cc = serializers.ListField(
        required=False,
        allow_null=True,
        default=['']
    )
    bcc = serializers.ListField(
        required=False, 
        allow_null=True,
        default=['']
    )
    
class IdMailValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    data = MailSerializer(required=False, allow_null=False)
    
    def validate(self, value):
        queryset = TemplateMail.objects.filter(id=value['id'])
        if not queryset.exists():
            raise serializers.ValidationError({'mail':ERROR['not_exists']})
        value['data'] = queryset.values()[0]
        return value