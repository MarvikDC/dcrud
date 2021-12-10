from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import Equipo, Document, privateDocument
#from . import models
from .forms import EquipoForm
from equiposv1 import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'crud/welcome.html')
    
@login_required(login_url='bienvenido')
def home(request):
    equipos = Equipo.objects.all()
    
    #{'equipos'<- Al template   :equipos<-Variable}
    context = {'equipos':equipos}
    return render(request, 'crud/home.html', context)

@login_required(login_url='bienvenido')
def equipos(request):
    equipos = Equipo.objects.all()
    return JsonResponse({'equipos':list(equipos.values())})

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

def helpdesk(request):
    if request.method == "POST":

        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " "  + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list=['mdelcarpiol@ulasalle.edu.pe']
        send_mail(subject, message, email_from, recipient_list)
        #user = request.user
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return redirect('bienvenido')
    
    return render(request, 'crud/helpdesk.html')


@login_required(login_url='bienvenido')
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

@login_required(login_url='bienvenido')
def privateFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = privateDocument(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = privateDocument.objects.all()

    return render(request, "crud/privateFiles.html", context = {
        "files": documents
    })

@login_required(login_url='bienvenido')
def detallefile(request, archivo_id):
    archivo = privateDocument.objects.get(id=archivo_id)
    texto=str(archivo.uploadedFile)
    ruta = texto.replace('static/','',1)
    context = {'ruta':ruta}
    return render(request, 'crud/renderfile.html', context)
    
    
    