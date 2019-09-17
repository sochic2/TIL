from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True)
    introduction = models.TextField(blank=True)
    

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')

