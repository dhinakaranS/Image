from django.db import models

# Create your models here.

class Image(models.Model):
    Userid = models.CharField(max_length = 30)
    Image_url = models.CharField(max_length = 60)
    title = models.CharField(max_length = 60)
    description = models.CharField(max_length = 1000)
    
