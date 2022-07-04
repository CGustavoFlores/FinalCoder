from django.urls import path, include
from AppPedidos.models import Clientes, Articulos, Marca, Pedidos, PedidoDetalle

from .import views 


urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path("listarclientes", views.listado_clientes, name="listar_clientes"),
    path('modificarcliente/<id>/',views.modificar_cliente, name="modificar_cliente"),
    path('eliminarcliente/<id>/', views.Eliminar_Cliente  , name ="Eliminar_cliente"), 
    path("clientes", views.abm_clientes, name="clientes"),
    #path("alta_clientes",views.alta_clientes),
    path("alta_clientes",views.alta_clienteForm, name = "altaclientes"),
    #path("articulos", views.abm_articulos, name = "articulos"),
    #path("alta_articulos", views.alta_articulos), 
    path("buscararticulo", views.buscar_articulos, name="buscararticulo"),
    path("buscar", views.buscar),
    path("contacto", views.contacto, name="contacto"),
    path("altaproducto", views.alta_producto, name="Alta_Producto"),
    path("listadoarticulo",views.listado_articulo, name="listar_articulo"),
    path('modificararticulo/<id>/',views.modificar_articulo, name="modificar_articulo"),
    path('eliminarproducto/<id>/', views.Eliminar_Articulo, name ="Eliminar_Articulo"), 
    path("about", views.about, name="about"),
    path("listadoPedidos",views.listar_pedidos, name="pedidos"),
    path("alta_pedido", views.alta_pedidoForm, name="altapedido"),
    path('modificarpedido/<id>/',views.modificar_pedido, name="modificar_pedido"),
    path('eliminarpedido/<id>/', views.Eliminar_Pedido, name="eliminarpedido"), 
             
       ]
