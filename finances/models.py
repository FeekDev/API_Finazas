# Modules
from django.db import models
from django.core.validators import RegexValidator
from datetime import time


# Model
class FinanzasPersonales(models.Model):
    '''
    Table is Finanzas_Personales

    Description:
    Have this fields to the table and
    have some validators to specific only
    the values needed
    '''
    nombreCompleto = models.CharField(blank=False, max_length=30)
    ingresosPersonales = models.IntegerField()
    fechaRegistro = models.TimeField(default=time)
    gastosMes = models.IntegerField()
    deudasTotales = models.IntegerField()
    pagoDeuda = models.IntegerField()

class Meta:
    ordering = ['nombreCompleto']