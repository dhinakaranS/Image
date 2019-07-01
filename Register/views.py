from django.shortcuts import render
from Register.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from cus_forms.register_form import RegisterForm

# Create your views here.
def registration(request):
    form =  RegisterForm()
    return render(request, 'register.html', {'form': form})


def saveUser(request):
    '''if(request.method == 'POST'):
    #     email = request.POST['email']
        fName = request.POST['first_name']
    #     lName = request.POST['last_name']
    #     uName = request.POST['username']
    #     passWord = request.POST['password']
    #     newUser = User()
    #     newUser.first_name = fName
    #     newUser.last_name = lName
    #     newUser.email = email
    #     newUser.user_name = uName
    #     newUser.password = passWord
    #     newUser.save()
    messages.success(request, 'Your profile was updated.') # ignored
    '''
    
    f = RegisterForm(request.POST)
    if(f.is_valid()):
        print('Success')
        return HttpResponseRedirect('/register')    
    else:
        return render(request, 'register.html', {'form': f})       
    
