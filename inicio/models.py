from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    publicacion = models.IntegerField()
    editorial = models.CharField(max_length=30)