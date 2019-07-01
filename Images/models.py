from django.conf import settings
from django.db import models
from django.utils import timezone
from Register.models import User



# Create your models here.

class Images(models.Model):
    Userid = models.ForeignKey(User,on_delete = models.CASCADE)
    Image_url = models.CharField(max_length = 60)
    title = models.CharField(max_length = 60)
    description = models.CharField(max_length = 1000)
    created_date = models.DateTimeField(default=timezone.now)

class Comments(models.Model):
    Userid = models.ForeignKey(User,on_delete = models.CASCADE)
    Imageid = models.ForeignKey(Images,on_delete = models.CASCADE)
    Comments = models.CharField(max_length = 150)
    
