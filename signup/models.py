from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=6)
    password=models.CharField(max_length=100)
    