from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import Equipo, Document
#from . import models
from .forms import EquipoForm
from equiposv1 import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
    equipos = Equipo.objects.all()
    
    #{'equipos'<- Al template   :equipos<-Variable}
    context = {'equipos':equipos}
    return render(request, 'crud/home.html', context)

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

def eliminar(request, equipo_id):
    equipo = Equipo.objects.get(id=equipo_id)
    equipo.delete()
    return redirect("home")

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


def helpdesk(request):
    if request.method == "POST":

        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " "  + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list=['mdelcarpiol@ulasalle.edu.pe']
        send_mail(subject, message, email_from, recipient_list)
        return redirect('home')
    
    return render(request, 'crud/helpdesk.html')

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = Document.objects.all()

    return render(request, "crud/upload-file.html", context = {
        "files": documents
    })
    
    
    