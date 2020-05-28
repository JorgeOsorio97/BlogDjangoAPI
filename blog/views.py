# Django Rest Framework
from rest_framework import viewsets, mixins

# Serializers
from blog.serializers import EntradaModelSerializer

# Models
from blog.models import Entrada
class EntradaModelViewSet(viewsets.ModelViewSet):

    queryset = Entrada.objects.all()
    serializer_class = EntradaModelSerializer
