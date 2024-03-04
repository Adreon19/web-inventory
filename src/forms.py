from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from .models import tbl_siswa
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput, EmailInput

class RegistsForm(UserCreationForm):
  username = forms.CharField(widget=TextInput(attrs={'class':'textbox','placeholder':'Username'}))
  email = forms.EmailField(widget=EmailInput(attrs={'class':'textbox','placeholder':'Email'}))
  password1 = forms.CharField(widget=PasswordInput(attrs={'class':'textbox','id':'password','placeholder':'Password'}))
  password2 = forms.CharField(widget=PasswordInput(attrs={'class':'textbox','id':'password','placeholder':'Confirm Password'}))
  class Meta:
    model = User
    fields = ["username","email","password1","password2"]
    
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput(attrs={'class':'textbox','placeholder':'Username'}))
  password = forms.CharField(widget=PasswordInput(attrs={'class':'textbox','id':'password','placeholder':'Password'}))
  class Meta:
    model = User
    fields = ["username","password"]
    
class UpdateUserProfile(forms.ModelForm):
  first_name = forms.CharField(max_length=100,required=False,label="Firstname")
  last_name = forms.CharField(max_length=100,required=False,label="Lastname")
  username = forms.CharField(max_length=100, required=True,label="Change Username")
  email = forms.EmailField(max_length=100, required=True,label="Change Email")
  
  class Meta:
    model = User
    fields = ["first_name","last_name","username","email"]
    
class PasswordChangeForm(PasswordChangeForm):
  class Meta:
    model = User
    fields = ['old_password','new_password1','new_password2']