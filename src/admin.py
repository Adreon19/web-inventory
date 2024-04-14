from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.

admin.site.site_header = "Administrator Panel"
admin.site.site_title = "Inventory"
admin.site.index_title = "Dashboard"

class ItemConfigAdmin(admin.ModelAdmin):
    list_display = ("name","category","condition","quantity","room", "image")
    list_filter = ["category","room","condition"]
    
class LendingConfigAdmin(admin.ModelAdmin):
    list_display = ("client","item","condition","room","lending_quantity","date_lending","return_time","status")
    list_filter = ["status"]

class CustomUserAdmin(UserAdmin):
    model = tbl_account
    list_display = ['username', 'first_name', 'last_name','email','phonenumber', 'is_staff', 'is_active', 'date_joined']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phonenumber')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'phonenumber', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('email', 'username', 'firstname', 'lastname', 'phonenumber')
    ordering = ('email',)

class FeedbackConfigAdmin(admin.ModelAdmin):
    list_display = ('subject', 'description','date')

admin.site.unregister(Group)
admin.site.register(tbl_feedback, FeedbackConfigAdmin)
admin.site.register(tbl_account, CustomUserAdmin)
admin.site.register(tbl_item, ItemConfigAdmin)
admin.site.register(tbl_loan, LendingConfigAdmin)