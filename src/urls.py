from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        path("",views.index, name="index"),
        path("accounts/",include("django.contrib.auth.urls")),
        path("accounts/signup",views.register, name="register"),
        path("accounts/logout/",auth_views.LogoutView.as_view,name="logout"),
        path("accounts/password_change/",auth_views.PasswordChangeView.as_view,name="password_change"),
        path("accounts/password_change/done/",auth_views.PasswordChangeDoneView.as_view,name="password_change_done"),
        path("accounts/password_reset/",auth_views.PasswordResetView.as_view,name="password_reset"),
        path("accounts/password_reset/done/",auth_views.PasswordResetDoneView.as_view,name='password_reset_done'),
        path("user/home/",views.home, name="home"),
        path("user/category/",views.category,name="category"),
        path("user/profile/",views.profile, name="profile"),
        path("user/order/",views.order,name="order"),
        path("user/history/",views.history,name="history")
]
