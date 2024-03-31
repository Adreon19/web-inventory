from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        path("",views.index, name="index"),
        path("accounts/login/",views.signin,name="login"),
        path("accounts/signup",views.register, name="register"),
        path("accounts/logout/",views.logouts,name="logout"),
        path("accounts/password_change/",views.change_password,name="password_change"),
        path("accounts/password_reset/",views.reset_password,name="password_reset"),
        path("user/home/",views.home, name="home"),
        path("user/category/",views.category,name="category"),
        path("user/category/<uuid:pk>",views.item_detail,name="item-detail"),
        path("user/profile/",views.profile, name="profile"),
        path("user/lending/",views.lending,name="lending"),
        path("user/history/",views.history,name="history")
]
