from django.core.files.storage import default_storage
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=250,null=True, blank=True)
    job = models.CharField(max_length=50,null=True, blank=True)
    image = models.ImageField(upload_to='media/avatar/',null=True, blank=True, default='default.png')
    fakulty = models.CharField(null=True,blank=True,max_length=50)
    yunalish = models.CharField(null=True,blank=True,max_length=50)
    gurux = models.CharField(null=True,blank=True,max_length=50)
    
class Fakulty(models.Model):
    name = models.CharField(null=True,blank=True,max_length=50)
    dek = models.CharField(null=True,blank=True,max_length=50)
    # def __init__(self,fak_id):
    #     self.fak_id = fak_id
    #
    # def fakultyid(self):
    #     print(self.fak_id)

class Yunalish(models.Model):
    name = models.CharField(null=True,blank=True,max_length=255)
    fakultet_id = models.IntegerField(null=True,blank=True)