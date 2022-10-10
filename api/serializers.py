from rest_framework import serializers
from .models import Oficio

class OficioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Oficio
        fields = (
            'cabecalho',
            'paragrafo_um',
            'paragrafo_dois',
            'rodape',
            'endereco',
            'telefone',
        )