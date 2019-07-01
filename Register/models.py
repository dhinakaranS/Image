from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,)
    email = models.CharField(max_length=30, unique=True)
    user_name  = models.CharField(max_length=30)
    password = models.CharField(max_length=20)    
    created_on = models.DateField(default=timezone.now)
    objects = UserManager()

    REQUIRED_FIELDS = ('password',)
    USERNAME_FIELD = 'email'
    is_authenticated = bool(True)
    is_anonymous = bool(False)

