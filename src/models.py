from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User,AbstractUser
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

MAJOR = (
  ("PPLG","PPLG"),
  ("DKV","DKV"),
  ("HOSPY","HOSPY"),
  ("AKUTANSI","AKUTANSI"),
)

CLASS = (
  (10,10),
  (11,11),
  (12,12)
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
  
class tbl_order(models.Model):
  client = models.ForeignKey(User, models.CASCADE,null=True)
  product = models.ForeignKey(tbl_barang, on_delete=models.CASCADE, null=True)
  order_quantity = models.PositiveIntegerField(null=True)
  date = models.DateTimeField(auto_now_add=True)

class tbl_siswa(models.Model):
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=100)
  jurusan = models.CharField(max_length=50,choices=MAJOR,null=True)
  kelas = models.IntegerField(choices=CLASS)
  nomortelp = PhoneNumberField(blank=True)
  email = models.EmailField()
  date_joined = models.DateTimeField(default=datetime.datetime.now)
  last_login = models.DateTimeField(blank=True,null=True)