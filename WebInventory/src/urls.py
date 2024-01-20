from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
        path("",views.home, name="home"),
        path("login/",views.login, name="login"),
        path("register/",views.register, name="register")
]
