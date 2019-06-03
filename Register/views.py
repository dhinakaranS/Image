from django.shortcuts import render
from Register.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def registration(request):
    return render(request,'register.html')

def saveUser(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        fName = request.POST['first_name']
        lName = request.POST['last_name']
        uName = request.POST['username']
        passWord = request.POST['password']
        newUser = User()
        newUser.first_name = fName
        newUser.last_name = lName        
        newUser.email = email
        newUser.user_name = uName
        newUser.password = passWord
        newUser.save()

    return HttpResponseRedirect('/login')

    
