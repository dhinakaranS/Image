from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,)
    email = models.CharField(max_length=30)
    user_name  = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    created_on = models.DateField(default=timezone.now)
