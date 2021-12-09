from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import loginForm, createUserForm
from django.contrib.auth import authenticate, login

# Create your views here.

def logear(request):
    username = request.POST['prueba3']
    password = request.POST['reastdyfugih1234']
    print(request.POST['username'])
    print(username)
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('home')
        
    else:
        return render(request, 'login.html')

        '''
    if request.method == "POST":
        #form = loginForm(request.GET)
        #usuario = request.GET.get('usuario')
        #contrasena = request.GET.get('contrasena')
        #print('###############################')
        #print(usuario)
        #print(contrasena)


        username = request.POST['usuario']
        password = request.POST['contrasena']
        
        if username != None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('debio logear')
                return redirect('home')
            else:
                print('es none')
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    '''
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
   

def index(request):
    return render(request, 'index.html')
