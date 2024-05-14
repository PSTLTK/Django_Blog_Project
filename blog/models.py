from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class PostModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default=None)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,default=None)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
