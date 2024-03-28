from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
import datetime

# Create your models here.

ITEMS = (
  ("Electronics","Electronics"),
  ("Cables","Cables"),
  ("Accessories","Accessories"),
  ("Other","Other")
)

ROOMS = (
  ("IT", "IT"),
  ("DKV","DKV")
)

CONDITION = (
  ("Normal","Normal"),
  ("Broken","Broken")
)

STATUS_CHOICES = (
  ('Diproses', 'Diproses'),
  ('Dikembalikan', 'Dikembalikan'),
  ('Ditolak', 'Ditolak'),
)

class tbl_barang(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100, null=True)
  category = models.CharField(max_length=100, choices=ITEMS, null=True)
  condition = models.CharField(max_length=100, choices=CONDITION, null=True)
  quantity = models.PositiveIntegerField(null=True)
  room = models.CharField(max_length=100, choices=ROOMS, null=True)
  image = models.ImageField(null=True,blank=True)
  
  def __str__(self):
    return f"{self.name}"
  
class tbl_peminjaman(models.Model):
  client = models.CharField(max_length=255,editable=False)
  item = models.ForeignKey(tbl_barang, on_delete=models.CASCADE, null=True)
  condition = models.CharField(max_length=100,choices=CONDITION,null=True)
  room = models.CharField(max_length=100,choices=ROOMS,null=True)
  lending_quantity = models.PositiveIntegerField(null=True)
  date_lending = models.DateTimeField(default=datetime.datetime.now,editable=False)
  return_time = models.DateTimeField(default=datetime.datetime.now)
  status = models.CharField(max_length=50,choices=STATUS_CHOICES,null=True)