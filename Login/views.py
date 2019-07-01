from django.shortcuts import render
from Register.models import User
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.
def viewHome(request):
    getUsers = User.objects.all()
    return render(request, 'login.html', {'users': getUsers})

def testMethod(request):
    email = request.POST['email']
    return  HttpResponse(email)

def authenticateUser(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=username, password=password)
    if user is not None:
        return  HttpResponse('Logged')
    else:
        return  HttpResponse('Not Logged')
    