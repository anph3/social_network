from django.db import models

class Logger(models.Model):
    class Meta:
        db_table = 'logger'
    id = models.BigAutoField(primary_key=True)
    user = models.IntegerField()
    method = models.CharField(max_length=50)
    event = models.CharField(max_length=255)
    input = models.CharField(max_length=255)
    output = models.CharField()
    event_time = models.DateTimeField()