from django.contrib import admin
from .models import Item, Order

# Register your models here.

admin.site.site_header = "Administrator Panel"
admin.site.site_title = "Web Inventory"
admin.site.index_title = "Dashboard"

class ItemAdmin(admin.ModelAdmin):
    list_display = ("name","category","condition","quantity","room")
    list_filter = ["category","room","condition"]
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ("client","product","order_quantity","date")

admin.site.register(Item,ItemAdmin)
admin.site.register(Order, OrderAdmin)