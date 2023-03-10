# Modulos
from rest_framework import serializers
from .models import FinanzasPersonales


class serializarCampos(serializers.ModelSerializer):
    class Meta:
        model = FinanzasPersonales
        fields = '__all__'