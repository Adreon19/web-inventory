from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from .models import *
from django.forms.widgets import PasswordInput, TextInput, EmailInput

from phonenumber_field.formfields import PhoneNumberField

class RegistsForm(UserCreationForm):
  username = forms.CharField(widget=TextInput(attrs={'class':'textbox','placeholder':'Username'}))
  email = forms.EmailField(widget=EmailInput(attrs={'class':'textbox','placeholder':'Email'}))
  password1 = forms.CharField(widget=PasswordInput(attrs={'class':'textbox','id':'password','placeholder':'Password'}))
  password2 = forms.CharField(widget=PasswordInput(attrs={'class':'textbox','id':'password','placeholder':'Confirm Password'}))
  class Meta:
    model = tbl_account
    fields = ["username","email","password1","password2"]
    
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput(attrs={'class':'textbox','placeholder':'Username'}))
  password = forms.CharField(widget=PasswordInput(attrs={'class':'textbox','id':'password','placeholder':'Password'}))
  class Meta:
    model = tbl_account
    fields = ["username","password"]
    
class UpdateUserProfile(forms.ModelForm):
  username = forms.CharField(max_length=100,required=True,label="Change username")
  first_name = forms.CharField(max_length=100,required=False,label="Change first name")
  last_name = forms.CharField(max_length=100,required=False,label="Change last name")
  email = forms.EmailField(max_length=100, required=True,label="Change Email")
  phonenumber = PhoneNumberField()
  
  class Meta:
    model = tbl_account
    fields = ["username","first_name", "last_name","email","phonenumber"]
    
class PasswordChangeForm(PasswordChangeForm):
  class Meta:
    model = tbl_account
    fields = ['old_password','new_password1','new_password2']

class ContactForm(forms.Form):
  class Meta:
    model = tbl_feedback
    field = ['subject','description']