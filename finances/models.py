from django.db import models
from django.core.validators import RegexValidator
from datetime import time

class Finanzas_Personales(models.Model):
    ID = models.IntegerField(primary_key=True, null=False)
    nombreCompleto = models.CharField(blank=False)
    ingresosPersonales = models.IntegerField()
    fechaRegistro = models.TimeField(default=time)
    gastosMes = models.IntegerField()
    deudasTotales = models.IntegerField()
    pagoDeuda = models.IntegerField()
