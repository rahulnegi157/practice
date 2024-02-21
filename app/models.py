from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.EmailField()