from rest_framework import serializers
from ..models.template_mail import *
from .action_seralizer import ActionSerializer
from django.db.models import Q
import bcrypt
from configs.variable_response import *

class MailSerializer(serializers.ModelSerializer, ActionSerializer):
    key = serializers.CharField(required=False, allow_null=True)
    
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
    
    class Meta:
        model = TemplateMail
        fields = ['id','key','title','body','created_at','updated_at','deleted_at']