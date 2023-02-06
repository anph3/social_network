from rest_framework import serializers
from ..models.game import Game
from .action_seralizer import ActionSerializer
from django.db.models import Q
from configs.variable_response import *

class GameSerializer(serializers.ModelSerializer, ActionSerializer):
    
    # ============================= function contructor =======================
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
    # ============================== end contructor ===========================
    
    # ============================== validate save ============================    
    # def validate_username(self, value):
    #     user = User.objects.filter(username=value)
    #     if user.exclude(deleted_at__isnull=True).exists():
    #         raise serializers.ValidationError(ERROR['dulicate_locked_user'])
    #     if user.filter(deleted_at__isnull=True).exists():
    #         raise serializers.ValidationError(ERROR['exists'])
    #     return value
    # =========================== end validate save ===========================
    
    class Meta:
        model = Game
        fields = ['id','game_name','key','status','created_at','updated_at','deleted_at']