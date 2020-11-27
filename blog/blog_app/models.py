from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title =  models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)