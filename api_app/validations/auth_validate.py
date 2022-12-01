from rest_framework import serializers

class LoginValidate(serializers.Serializer):
    username = serializers.CharField(min_length=6)
    password = serializers.CharField(min_length=6)
    
class RefreshTokenValidate(serializers.Serializer):
    refresh_token = serializers.CharField()