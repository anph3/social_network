from rest_framework import serializers
from ..models.user import *
from .action_seralizer import ActionSerializer
from django.db.models import Q
import bcrypt
from configs.variable_response import *

class UserSerializer(serializers.ModelSerializer, ActionSerializer):
    username = serializers.CharField(min_length=6)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)
    
    # ============================= function contructor =======================
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        not_fields = kwargs.pop('not_fields', None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if not_fields is not None:
            for field_name in not_fields:
                self.fields.pop(field_name)
    # ============================== end contructor ===========================
    
    # ============================== validate save ============================    
    def validate_username(self, value):
        user = User.objects.filter(username=value)
        if user.exclude(deleted_at__isnull=True).exists():
            raise serializers.ValidationError(ERROR['dulicate_locked_user'])
        if user.filter(deleted_at__isnull=True).exists():
            raise serializers.ValidationError(ERROR['exists'])
        return value
    
    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user.exclude(deleted_at__isnull=True).exists():
            raise serializers.ValidationError(ERROR['dulicate_locked_user'])
        if user.filter(deleted_at__isnull=True).exists():
            raise serializers.ValidationError(ERROR['exists'])
        return value
        
    def validate_password(self, value):
        return self.hash_password(value).decode('utf-8')
    
    def hash_password(self, s):
        byte_pwd = s.encode('utf-8')
        my_salt = bcrypt.gensalt()
        pwd_hash = bcrypt.hashpw(byte_pwd, my_salt)
        return pwd_hash
    # =========================== end validate save ===========================
    
    class Meta:
        model = User
        fields = ['id','username','email','password','created_at','updated_at','deleted_at']