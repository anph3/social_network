from django.db import models

class Game(models.Model):
    class Meta:
        db_table = 'game'
    id = models.BigAutoField(primary_key=True)
    game_name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()