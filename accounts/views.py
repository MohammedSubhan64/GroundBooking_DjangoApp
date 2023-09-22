from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required
# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("password doesnot match")
        else:
            user=User.objects.create_user(username,email,password1)
            user.save()
            return redirect('login')
    return render(request,'login.html')

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('user')
        else:
            return HttpResponse("username or password is incorrect!!!")
    return render(request,'login.html')

# @login_required(login_url='login')
def user(request):
    return render(request,'user.html')

def logoutpage(request):
    logout(request)
    return redirect('login')