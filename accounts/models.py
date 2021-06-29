from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=250,null=True, blank=True)
    job = models.CharField(max_length=50,null=True, blank=True)
    image = models.ImageField(upload_to='madia/users/',null=True, blank=True)