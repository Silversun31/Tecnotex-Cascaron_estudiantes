from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.API import viewsets

router = DefaultRouter()
router.register('pedido', viewsets.PedidoViewSet, 'pedidos')
urlpatterns = [
    path('', include(router.urls)),
]
