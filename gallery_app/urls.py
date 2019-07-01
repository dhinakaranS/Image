"""gallery_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Login import views as log
from Register import views as reg
from Images import views as img

urlpatterns = [
    path('',log.viewHome),
    path('login/',log.viewHome),
    path('admin/', admin.site.urls),
    path('register/',reg.registration),
    path('gallery/',img.image_gallery),
    path('gallery/newimage/', img.new),
    path('gallery/comments/<int:id>/', img.comments),
    path('register/user', reg.saveUser),
    path('gallery/newimage/image',img.saveimage),
    path('authenticate', log.authenticateUser)
    
]
