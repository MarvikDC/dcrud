from django.db import models

# Create your models here.

class Evento(models.Model):
    
    equipo_id = models.IntegerField()
    evento_descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.equipo_id + "  "+ self.evento_descripcion