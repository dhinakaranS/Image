from django.contrib import admin
from user.models import Username,email

admin.site.Register(Username)
admin.site.Register(email)


# Register your models here.
