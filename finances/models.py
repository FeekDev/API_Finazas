# Modules
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import time

def validador_ingresos(value):
    maximo_permitido = 3000000
    if value > maximo_permitido:
        raise ValidationError(
            message=f'el valor ingresado {value}, es mayor al permitido ')

# Model
class FinanzasPersonales(models.Model):
    '''
    Table is Finanzas_Personales

    Description:
    Have this fields to the table and
    have some validators to specific only
    the values needed
    '''
    nombreCompleto = models.CharField(
        blank=False, 
        max_length=30, 
        validators=[RegexValidator(
            regex='^[a-zA-Z ]+$', 
            message='el formato no está permitido, solo letras')])
    ingresosPersonales = models.IntegerField(
        blank=False,
        validators=[validador_ingresos],
    )
    fechaRegistro = models.TimeField(default=time)
    gastosMes = models.IntegerField()
    deudasTotales = models.IntegerField()
    pagoDeuda = models.IntegerField()

class Meta:
    ordering = ['nombreCompleto']