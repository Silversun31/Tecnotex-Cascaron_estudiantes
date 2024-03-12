from rest_framework import serializers
from apps.core import models as core_models


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Pedido
        fields = (
            'numero_pedido', 'fecha_entrada', 'financiamiento', 'total_suministro', 'estado', 'gastos_operacionales',
            'total_general')
