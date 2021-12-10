from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import loginForm, createUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='bienvenido')
def crearusuario(request):
    if request.method == "POST":
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logear')
    else:
        form = createUserForm()

    context = {'form' : form}
    return render(request, 'createUser.html', context)
   
