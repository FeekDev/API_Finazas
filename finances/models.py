# Modules
from django.db import models
from django.core.validators import RegexValidator
from datetime import time


# Model
class Finanzas_Personales(models.Model):
    '''
    Table is Finanzas_Personales

    Description:
    Have this fields to the table and
    have some validators to specific only
    the values needed
    '''
    ID = models.IntegerField(primary_key=True, null=False)
    nombreCompleto = models.CharField(blank=False)
    ingresosPersonales = models.IntegerField()
    fechaRegistro = models.TimeField(default=time)
    gastosMes = models.IntegerField()
    deudasTotales = models.IntegerField()
    pagoDeuda = models.IntegerField()
