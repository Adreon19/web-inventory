from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, "index.html")

def login(request):
    if (request.method == "POST"): pass
    return render(request, "login.html")

def register(request):
    if request.method == "POST": 
        user = request.POST.get('username')
        mail = request.POST.get('email')
        passwd = request.POST.get('password')
        confirm = request.POST.get('confirmPass')

        if User.objects.filter(username=user):
            messages.error(request, "username sudah teregistrasi!!")

        if User.objects.filter(email=mail):
            messages.error(request, "email sudah teregistrasi!!")

        if (confirm != passwd):
            messages.error(request,"password tidak sama!!")

        reguser = User.objects.create_user(user,mail,passwd)

        reguser.username = user
        reguser.save()

        messages.success(request,"akun mu sudah teregistrasi!!")

        return redirect("/login")

    return render(request, "register.html")
