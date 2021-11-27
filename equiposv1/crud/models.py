from django.db import models

# Create your models here.

class Equipo(models.Model):
    
    equipo_serie = models.CharField(max_length=100)
    equipo_marca = models.CharField(max_length=20)
    equipo_descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.equipo_serie + "  "+ self.equipo_marca+ "  "+ self.equipo_descripcion
        

class Document(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)


