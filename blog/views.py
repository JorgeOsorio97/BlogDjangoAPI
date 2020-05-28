# Django Rest Framework
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from blog.serializers import EntradaModelSerializer

# Models
from blog.models import Entrada


class EntradaModelViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaModelSerializer


class FakeLogin (APIView):
    def post(self, request):
        data = request.data
        if data['usuario'] == "admin" and data['pass'] == "admin1234":
            return Response({'success': True, 'message': ""})
        return Response({'success': False, 'message': "Accesos invalidos"})