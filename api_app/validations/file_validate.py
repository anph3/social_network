from rest_framework import serializers
from django.conf import settings
import os
from configs.variable_response import *

class FileDownloadValidate(serializers.Serializer):
    id = serializers.CharField()
    type = serializers.CharField(required=False, allow_null=True)

    def validate(self, value):
        if not os.path.exists(os.path.join(settings.MEDIA_ROOT, str(value['id']))):
            raise serializers.ValidationError({'File name':ERROR['not_exists']})
        name = str(value['id']).split('.')
        if not str(name[0]).split('_')[0].isdigit():
            raise serializers.ValidationError({'File name':'not_exists'})
        value['id'] = name[0]
        value['type'] = name[-1]
        return value
        
    