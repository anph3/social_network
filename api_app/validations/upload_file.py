from rest_framework import serializers
from configs.variable_response import *

class FileValidate(serializers.Serializer):
    file = serializers.ListField(
        child = serializers.FileField()
    )