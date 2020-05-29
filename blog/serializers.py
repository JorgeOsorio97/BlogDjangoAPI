# Standard library
from datetime import datetime
# Django Rest Framework
from rest_framework import serializers

# Models
from blog.models import Entrada

class EntradaModelSerializer(serializers.ModelSerializer):

    fecha_publ = serializers.SerializerMethodField()

    def get_fecha_publ(self, obj: Entrada) -> datetime:
        return datetime.timestamp(obj.fecha_publ)

    class Meta:
        model = Entrada
        fields = (
            'id',
            'titulo',
            'texto_intro',
            'texto_completo',
            'imagen',
            'fecha_publ'
        )
        read_only_fields = ('id', 'fecha_publ')