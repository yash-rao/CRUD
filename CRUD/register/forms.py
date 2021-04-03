from django import forms
from django.db.models import fields
from django.forms import widgets
from register.models import User
from django.core import validators

class Studentform(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }