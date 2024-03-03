from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "Administrator Panel"
admin.site.site_title = "Web Inventory"
admin.site.index_title = "Dashboard"

class ItemConfigAdmin(admin.ModelAdmin):
    list_display = ("name","category","condition","quantity","room")
    list_filter = ["category","room","condition"]
    
class OrderConfigAdmin(admin.ModelAdmin):
    list_display = ("client","product","order_quantity","date")

class SiswaConfigAdmin(admin.ModelAdmin):
    list_display = ("username","jurusan","kelas","nomortelp","email","date_joined","last_login")
    list_filter = ["jurusan","kelas"]

admin.site.register(tbl_barang,ItemConfigAdmin)
admin.site.register(tbl_order, OrderConfigAdmin)
admin.site.register(tbl_siswa,SiswaConfigAdmin)