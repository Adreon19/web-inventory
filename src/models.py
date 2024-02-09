from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ITEMS = (
  ("Electronics","Electronics"),
  ("Cables","Cables"),
  ("Accessories","Accessories")
)

class Item(models.Model):
  name = models.CharField(max_length=100, null=True)
  category = models.CharField(max_length=100, choices=ITEMS, null=True)
  quantity = models.PositiveIntegerField(null=True)
  image = models.ImageField(null=True,blank=True)
  
  def __str__(self):
    return f"{self.name}"
  
class Order(models.Model):
  client = models.ForeignKey(User, models.CASCADE,null=True)
  product = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
  order_quantity = models.PositiveIntegerField(null=True)
  date = models.DateTimeField(auto_now_add=True)