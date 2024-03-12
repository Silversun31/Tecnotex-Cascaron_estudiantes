from rest_framework import viewsets, permissions

from apps.API import serializers
from apps.core import models as core_models


class PedidoViewSet(viewsets.ModelViewSet):
    """
    Permitir las operaciones CRUD sobre la tabla Pedido
    """
    queryset = core_models.Pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.PedidoSerializer
    http_method_names = ['get', 'head', 'post', 'put', 'patch']
