from django import forms
from django.forms import fields
from django.contrib.auth.models import User

class loginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class createUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email','first_name','last_name','username', 'password', 'is_staff' ]
        

