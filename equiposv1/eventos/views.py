from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

#from equiposv1 import eventos
from .models import Evento
from crud.models import Equipo

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView



#@login_required(login_url='bienvenido')
def homeeventos(request):
    evento = Evento.objects.all()
    
    #{'equipos'<- Al template   :equipos<-Variable}
    context = {'evento': evento}
    return render(request, 'evento.html', context)

def listaeventos(request):
    equipos = Equipo.objects.all()
    eventos = Evento.objects.all()
    leventos = list(eventos.values())
    lequipos = list(equipos.values())
    lideq=[]
    lidev=[]
    for x in range(len(lequipos)):
        lideq.append(lequipos[x]['id'])

    for x in range(len(leventos)):
        lidev.append(leventos[x]['equipo_id'])

    vista = []
    print(len(leventos))
    for x in range(0,len(leventos)):
        print('esto es'+ str(x))
        evento={}
        requipo = Equipo.objects.get(id=leventos[x]['equipo_id'])
        print(requipo.id)

        uevento = leventos[x]['evento_descripcion']
        evento['equipo_id']=requipo.id
        evento['equipo_serie']=requipo.equipo_serie
        evento['equipo_serie']=requipo.equipo_descripcion

        evento['ev']=uevento

        vista.append(evento)
    
    return JsonResponse({'vista':vista})

'''
@login_required(login_url='bienvenido')
def eliminar(request, equipo_id):
    equipo = Equipo.objects.get(id=equipo_id)
    equipo.delete()
    # return redirect("home")
    return JsonResponse({'status': "deleted"})

#-----------------------------------------------------------

@login_required(login_url='bienvenido')
def agregar(request):
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EquipoForm()

    context = {'form' : form}
    return render(request, 'crud/agregar.html', context)

@login_required(login_url='bienvenido')
def eliminar(request, equipo_id):
    equipo = Equipo.objects.get(id=equipo_id)
    equipo.delete()
    # return redirect("home")
    return JsonResponse({'status': "deleted"})

@login_required(login_url='bienvenido')
def editar(request, equipo_id):
    equipo = Equipo.objects.get(id=equipo_id)
    if request.method == "POST":
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EquipoForm(instance=equipo)

    context = {'form' : form}
    return render(request, 'crud/editar.html', context)

'''