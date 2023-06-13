from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
                print("User Created")
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        #return redirect('/')

    return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home/postlogin')
        else:
            messages.info(request, "invalid Credentials")
            return redirect('login')

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/home/homepage')