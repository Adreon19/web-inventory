from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *
from .models import *

from django.views.decorators.csrf import csrf_protect

# Create your views here.

def index(request):
    return render(request, "core/index.html")

@csrf_protect
@login_required
def home(request):
    return render(request,"users/home.html")

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
        forms = LoginForm(data=request.POST)
        if forms.is_valid():
            """
            user = forms.get_user()
            login(request, user)
            return redirect('src:home')  # Redirect to dashboard after login
            """
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('src:home') 
    else:
        forms = LoginForm()
        
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
        display= tbl_item.objects.filter(room=rooms,condition=condition)
        return render(request,"users/category.html",{"Items":display})
    else:
        search = tbl_item.objects.filter()
        return render(request,"users/category.html",{"Items":search})

@login_required
def order(request):
    return render(request, "users/order.html", {"borrow":tbl_lend.objects.all()})

@login_required
def history(request):
    context = {
        "peminjaman":tbl_lend.objects.all()
    }
    return render(request, "users/history.html",context)

def item_detail(request,pk):
    item = tbl_item.objects.get(pk=pk)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        user = request.POST['username']
        condition = request.POST['condition']
        room = request.POST['room']
        if quantity <= item.quantity: 
            order = tbl_lend(
                item=item, 
                client=get_object_or_404(tbl_account, username=user),
                lending_quantity=quantity, 
                condition=condition,
                room=room,
                status="Diproses"
            )
            order.save()
            item.quantity -= quantity
            item.save()
            return redirect('src:history')
        else:
            error_message = "Insufficient quantity available"
            return render(request, 'core/item_detail.html', {'item': item, 'error_message': error_message})
    return render(request, 'core/item_detail.html', {'item': item})
