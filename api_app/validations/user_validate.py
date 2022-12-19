from rest_framework import serializers
from ..models.user import User
from configs.variable_response import *
from ..serializers.user_serializer import *

class IdGetUserValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    data = UserSerializer(required=False, allow_null=False)
    
    def validate(self, value):
        queryset = User.objects.filter(id=value['id'])
        if not queryset.exists():
            raise serializers.ValidationError({'user':ERROR['not_exists']})
        value['data'] = queryset.values()[0]
        return value