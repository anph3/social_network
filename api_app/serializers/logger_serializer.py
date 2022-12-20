from rest_framework import serializers
from ..models.logger import Logger

class LoggerSerializer(serializers.ModelSerializer):
    
    user = serializers.IntegerField(required=False, allow_null=True)
    method = serializers.CharField(required=False, allow_null=True)
    event = serializers.CharField(required=False, allow_null=True)
    input = serializers.CharField(required=False, allow_null=True)
    output = serializers.CharField(required=False, allow_null=True)
    event_time = serializers.DateTimeField(required=False, allow_null=True)
    
    class Meta:
        model = Logger
        fields = ['id','user','method','event','input','output','event_time']