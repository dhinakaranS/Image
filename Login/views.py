from django.shortcuts import render
from Register.models import User
from django.http import HttpResponse

# Create your views here.
def viewHome(request):
    getUsers = User.objects.all()
    return render(request, 'login.html', {'users': getUsers})

def testMethod(request):
    email = request.POST['email']
    return  HttpResponse(email)