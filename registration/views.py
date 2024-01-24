from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from .models import Cloth
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
   # cloths = Cloth.objects.all()
   #{'cloths': cloths}, in render temlates
    username = request.user.username
    email = request.user.email
    return render(request, 'home.html', {'username': username, 'email': email})

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Your password and confirm password are not the same!")
            return render(request, 'sign.html')

        try:
            existing_user = User.objects.get(username=uname)
            messages.error(request, "Username already in use. Please choose another username.")
            return render(request, 'sign.html')
        except User.DoesNotExist:
            pass

        try:
            existing_email = User.objects.get(email=email)
            messages.error(request, "Email already in use. Please use a different email address.")
            return render(request, 'sign.html')
        except User.DoesNotExist:
            pass

        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()

        messages.success(request, "Account created successfully. You can now login.")
        return redirect('login')

    return render(request, 'sign.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect!!!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('index')
