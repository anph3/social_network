from rest_framework import serializers
from ..models.user import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','password','created_at','updated_at','deleted_at']