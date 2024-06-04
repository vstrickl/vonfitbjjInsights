from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FacebookToken(models.Model):
    token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Token created {self.created_at}'

class FacebookPage(models.Model):
    page_id = models.CharField(max_length=255, unique=True)
    ig_user_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    cli_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255)
    category_list = models.JSONField()

    def __str__(self):
        return self.name