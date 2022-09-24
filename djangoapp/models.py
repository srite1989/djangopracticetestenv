from pyexpat import model
from re import U
from django.db import models
from django.contrib.auth.models import AbstractUser

class LoginUser(AbstractUser):
    username=models.CharField(max_length=20,unique=True,blank=True)
    orname=models.CharField(max_length=50,blank=True)
    ortype=models.CharField(max_length=50,blank=True)
    email=models.EmailField(max_length=50,blank=True)
    password=models.CharField(max_length=20,blank=True)
    class Meta:
        db_table='user'