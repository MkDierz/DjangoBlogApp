from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
<<<<<<< HEAD
        login(request, newUser)
        messages.info(request, "Başarıyla Kayıt Oldunuz...")
=======
        login(request,newUser)
        messages.info(request,"You have successfully registered")
>>>>>>> b19a82f1d410c419cd0f0f3ad96bb51466c08a2c

        return redirect("index")
    context = {
        "form": form
    }
    return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
<<<<<<< HEAD
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı")
            return render(request, "login.html", context)

        messages.success(request, "Başarıyla Giriş Yaptınız")
        login(request, user)
=======
            messages.info(request,"Username or Password Incorrect")
            return render(request,"login.html",context)

        messages.success(request,"You have successfully logged in.")
        login(request,user)
>>>>>>> b19a82f1d410c419cd0f0f3ad96bb51466c08a2c
        return redirect("index")
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
<<<<<<< HEAD
    messages.success(request, "Başarıyla Çıkış Yaptınız")
=======
    messages.success(request,"You have successfully logged out")
>>>>>>> b19a82f1d410c419cd0f0f3ad96bb51466c08a2c
    return redirect("index")
