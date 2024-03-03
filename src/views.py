from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from .forms import *
from .models import *

from django.views.decorators.csrf import csrf_protect

# Create your views here.

def index(request):
    return render(request, "core/index.html")

@csrf_protect
@login_required
def home(request):
    context = {"products":tbl_barang.objects.all()}
    return render(request,"users/home.html",context)

def register(request):
    if request.method == "POST": 
        forms = RegistsForm(request.POST or None)
        if forms.is_valid():
            forms.save()
            return redirect("src:login")
    else:
        forms = RegistsForm()

    return render(request, "registration/register.html",{"form":forms})

def signin(request):
    if request.method == 'POST':
        forms = LoginForm(request, data=request.POST)
        if forms.is_valid():
            users = forms.get_user()
            login(request,users)
            return redirect("src:home")
    else:
        forms = LoginForm(request)
        
    return render(request,"registration/login.html",{"form":forms})

def logouts(request):
    if request.method == 'POST':
        logout(request)
        return redirect("src:login")
    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("src:home")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,"registration/password_change.html",{"form":form})

def reset_password(request):
    return render(request, "registration/password_reset_form.html")

@login_required
def profile(request):
    if (request.method == "POST"):
        userprof = UpdateUserProfile(request.POST , instance=request.user)
        if userprof.is_valid():
            userprof.save()
            return redirect("src:profile")
    else:
        userprof = UpdateUserProfile(instance=request.user)
        
    return render(request,"users/profile.html",{"editform":userprof})

@login_required
def category(request):
    if (request.method == "POST"):
        rooms = request.POST.get("room")
        condition = request.POST.get("condition")
        display= tbl_barang.objects.filter(room=rooms,condition=condition)
        return render(request,"users/category.html",{"Items":display})
    else:
        search = tbl_barang.objects.filter()
        return render(request,"users/category.html",{"Items":search})

@login_required
def order(request):
    return render(request, "users/order.html")

@login_required
def history(request):
    context = {
        "peminjaman":tbl_peminjaman.objects.all()
    }
    return render(request, "users/history.html",context)
