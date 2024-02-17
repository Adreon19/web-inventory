from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistsForm, UpdateUserProfile,LoginForm
from .models import Item

from django.views.decorators.csrf import csrf_protect

# Create your views here.

def index(request):
    return render(request, "core/index.html")

@csrf_protect
@login_required
def home(request):
    context = {"products":Item.objects.all()}
    return render(request,"users/home.html",context)

def register(request):
    if request.method == "POST": 
        forms = RegistsForm(request.POST or None)
        if forms.is_valid():
            forms.save()
            client = forms.cleaned_data.get('username')
            messages.success(request,f"Create account success for {client}. Continue to login")
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
        display= Item.objects.filter(room=rooms,condition=condition)
        return render(request,"users/category.html",{"Items":display})
    else:
        search = Item.objects.filter()
        return render(request,"users/category.html",{"Items":search})

@login_required
def order(request):
    return render(request, "users/order.html")

@login_required
def history(request):
    return render(request, "users/history.html")
