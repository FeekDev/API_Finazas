# Modules
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.timezone import now

DATE_FORMAT = '%d/%M/%Y'

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
    fechaRegistro = models.DateField(auto_now=True)
    gastosMes = models.IntegerField(
        blank=False)
    deudasTotales = models.IntegerField(blank=False)
    pagoDeuda = models.IntegerField(blank=False)


class Meta:
    ordering = ['nombreCompleto']

def datepublished(self):
        return self.pub_date.strftime('%d/%M/%Y')