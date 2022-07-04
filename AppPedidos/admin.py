from django.contrib import admin

from AppUsuario.models import Avatar

# Register your models here.
from .models import Clientes, Marca, Articulos, Pedidos, PedidoDetalle, Contacto

admin.site.register(Marca)
admin.site.register(Articulos)
admin.site.register(Clientes)
admin.site.register(Pedidos)
admin.site.register(PedidoDetalle)
admin.site.register(Contacto)
admin.site.register(Avatar)