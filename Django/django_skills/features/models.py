from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Info(models.Model):

    name=models.CharField(max_length=400)
    contact=models.CharField(max_length=400)
    interests=models.CharField(max_length=400)
