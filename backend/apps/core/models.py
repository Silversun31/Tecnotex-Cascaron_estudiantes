from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
TIPOS_FINANCIAMIENTO = (('liquido', 'Liquido'), ('360', '360'), ('540', '540'), ('720', '720'))
ESTADOS = (('presentado', 'Presentado'), ('recibido', 'Recibido'), ('pendiente', 'Pendiente a salir al mercado'),
           ('rechazado', 'Rechazado'))
GASTOS_EXTRAS_OPERACIONALES = 20
GASTOS_EXTRAS_GENERALES = 10


class Pedido(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    fecha_entrada = models.DateTimeField('Fecha de Entrada en Tecnotex')
    # numero 711/OC(identificador)
    financiamiento = models.CharField(verbose_name='Financiamiento', choices=TIPOS_FINANCIAMIENTO, max_length=254)
    total_suministro = models.FloatField(verbose_name='Total de Suministro', validators=[MinValueValidator(0)])
    estado = models.CharField(verbose_name='Estado', auto_created=True, default='presentado', choices=ESTADOS,
                              max_length=254)

    def gastos_operacionales(self):
        return self.total_suministro + GASTOS_EXTRAS_OPERACIONALES

    def total_general(self):
        return self.gastos_operacionales() + GASTOS_EXTRAS_GENERALES
