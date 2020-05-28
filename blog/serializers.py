# Django Rest Framework
from rest_framework import serializers

# Models
from blog.models import Entrada

class EntradaModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Entrada
        fields = (
            'titulo',
            'texto_intro',
            'texto_completo',
            'imagen',
        )