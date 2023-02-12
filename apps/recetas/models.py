from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Receta(models.Model):
    persona       = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default='')
    nombre        = models.CharField(max_length=200)
    ingredientes  = models.TextField()
    modo_preparacion = models.TextField()
    tiempo_preparacion = models.IntegerField()
    rendimento    = models.CharField(max_length=100)
    categoria     = models.CharField(max_length=100)
    data_criacao  = models.DateTimeField(default=datetime.now, blank=True)
    foto          = models.ImageField(upload_to='recetas/fotos/', blank=True)
    publicada     = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre

class LogReceta(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.SET_NULL, null=True)
    user = models.CharField(max_length=50, null=False)
    fecha = models.DateTimeField(null=False)
    accion = models.CharField(max_length=50, null=False)

