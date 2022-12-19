from django.db import models

class TemplateMail(models.Model):
    class Meta:
        db_table = 'template_mail'
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)    
    deleted_at = models.DateTimeField()