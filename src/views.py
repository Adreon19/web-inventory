from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistsForm, UpdateUserProfile
from .models import Item

from django.views.decorators.csrf import csrf_protect

# Create your views here.

def index(request):
    return render(request, "index.html")

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
            return redirect("src:login")
    else:
        forms = RegistsForm()

    return render(request, "registration/register.html",{"form":forms})

@login_required
def profile(request):
    if (request.method == "POST"):
        userprof = UpdateUserProfile(request.POST , instance=request.user)
        if userprof.is_valid():
            userprof.save()
            return redirect("src:home")
    else:
        userprof = UpdateUserProfile(instance=request.user)
        
    return render(request,"users/profile.html",{"editform":userprof})

@login_required
def order(request):
    return render(request, "users/order.html")
