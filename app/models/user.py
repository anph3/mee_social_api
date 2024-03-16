from django.db import models
from ..managers import user_manager as um

class User(models.Model):
    class Meta:
        db_table = 'user'
    id = models.BigAutoField(primary_key=True)
    display_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()
    
    objects = um.UserManager()