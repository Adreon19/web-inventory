from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.

admin.site.site_header = "Administrator Panel"
admin.site.site_title = "Inventory"
admin.site.index_title = "Dashboard"

class ItemConfigAdmin(admin.ModelAdmin):
    list_display = ("name","category","condition","quantity","room")
    list_filter = ["category","room","condition"]
    
class LendingConfigAdmin(admin.ModelAdmin):
    list_display = ("client","item","condition","room","lending_quantity","date_lending","return_time","status")


admin.site.unregister(Group)
admin.site.register(tbl_barang,ItemConfigAdmin)
admin.site.register(tbl_peminjaman, LendingConfigAdmin)