from pkgutil import ImpImporter
from re import I
from urllib import request
from urllib.request import Request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.template import loader
from AppPedidos.forms import AbmCliente_formulario, AbmArticulo_formulario, AbmPedido_formulario
from .forms import ContactoForm, PedidoForm, ProductoForm, ClienteForm
from AppPedidos.models import Clientes, Articulos, Pedidos, PedidoDetalle, Marca
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required


# Create your views here.



def Inicio(request):
    return render(request,"menu.html")


def about(request):
    return render(request, "about.html")



def leer_clientes(request):
    clientes = Clientes.objects.all()
    texto = "leerclientes"
    return  HttpResponse( clientes )

def abm_clientes(request):
    return render(request, "abmclientes.html")



def buscar(request):
    if request.GET['nombre']:
        page = request.GET.get('pagina')
        nombre = request.GET.get('nombre')
        articu = Articulos.objects.filter(Descripcion__icontains = nombre)
        page = request.GET.get('page',1)
        
        try:
            paginator = Paginator(articu,3)
            articu=paginator.page(page)
        except:
            raise Http404
            
        data = {
            'entity': articu,
            'paginator': paginator
            
        }
        return render( request, "articulos/resultado_buscararticulo.html" , data)
        #return HttpResponse (f"Estamos buscadno { request.GET['nombre']}")
    else:
        return HttpResponse ("campo de busqueda vacio")
        
        
        
        
        
def contacto(request):
    data ={
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Contacto guardado"
        else:
            data["form"] = formulario
    
    return render (request, 'contacto.html', data)



def alta_producto(request):
    data =  {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Alta OK!!")
            #data["mensaje"]="El articulo fue grabado OK !!"
        else:
            data["form"]= formulario
    return render(request, 'articulos/altaarticulo.html', data )




def listado_articulo(request):
    productos = Articulos.objects.all()
    page= request.GET.get('page',1)
    try:
        paginator = Paginator(productos,5)
        productos=paginator.page(page)
    except:
        raise Http404
            
    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'articulos/listadoarticulo.html', data)







def modificar_articulo(request, id):
    producto  = get_object_or_404( Articulos , id = id)
    data = {
         'form': ProductoForm(instance=producto)
    }    
    if request.method == 'POST':
        formulario = ProductoForm (data = request.POST, instance = producto, files=request.FILES)
        if formulario.is_valid():
            messages.success(request, "Modificacion OK!!")
            formulario.save()
            return redirect(to="listar_articulo")
            data["form"]=formulario
    else :           
        print("NO entro al post")
    return render (request, 'articulos/modificaArticulo.html', data)



def Eliminar_Articulo(request, id):
    producto= get_object_or_404(Articulos,id=id)
    producto.delete()
    messages.success(request, "Eliminacion OK!!")
    return redirect(to="listar_articulo")





def alta_clienteForm(request):
    data =  {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Alta OK!!")
            #data["mensaje"]="El articulo fue grabado OK !!"
        else:
            data["form"]= formulario
    return render(request, 'clientes/altaClientes.html', data )



@login_required( login_url="/AppUsuario/Login" )
def listado_clientes(request):
    clientes = Clientes.objects.all()
    page= request.GET.get('page',1)
    try:
        paginator = Paginator(clientes,5)
        clientes=paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': clientes,
        'paginator': paginator
    }
    return render(request, 'clientes/listadoClientes.html', data)


@login_required( login_url="/AppUsuario/Login" )
def modificar_cliente(request, id):
    cliente  = get_object_or_404(Clientes , id = id)
    data = {
         'form': ClienteForm(instance=cliente)
    }    
    if request.method == 'POST':
        formulario = ClienteForm (data = request.POST, instance = cliente, files=request.FILES)
        if formulario.is_valid():
            messages.success(request, "Modificacion OK!!")
            formulario.save()
            return redirect(to="listar_clientes")
            data["form"]=formulario
    else :           
        print("NO entro al post")
    return render (request, 'clientes/modificarcliente.html', data)



@login_required( login_url="/AppUsuario/Login" )
def Eliminar_Cliente(request, id):
    cliente= get_object_or_404(Clientes,id=id)
    cliente.delete()
    messages.success(request, "Eliminacion OK!!") 
    return redirect(to="listar_clientes")






def listar_pedidos(request):
    pedidos = Pedidos.objects.all()    
    page= request.GET.get('page',1)
    try:
        paginator = Paginator(pedidos,5)
        pedidos=paginator.page(page)
    except:
        raise Http404        
    data = {
        'entity': pedidos,
        'paginator': paginator
    }
    return render(request, 'pedidos/listarPedidos.html', data)



def alta_pedidoForm(request):
    data =  {
        'form': PedidoForm()
    }
    if request.method == 'POST':
        formulario =  PedidoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Nuevo Pedido OK!!")
            #data["mensaje"]="El articulo fue grabado OK !!"
        else:
            data["form"]= formulario       
    return render(request, 'pedidos/AltaPedido.html', data )




def modificar_pedido(request, id):
    pedido  = get_object_or_404(Pedidos , id = id)
    data = {
         'form': PedidoForm(instance=pedido)
    }    
    if request.method == 'POST':
        formulario = PedidoForm (data = request.POST, instance = pedido, files=request.FILES)
        if formulario.is_valid():
            messages.success(request, "Modificacion Pedido OK!!")
            formulario.save()
            return redirect(to="pedidos")
            data["form"]=formulario
    else :           
        print("NO entro al post")
    return render (request, 'pedidos/modificarPedido.html', data)



def Eliminar_Pedido(request, id):
    pedi = get_object_or_404(Pedidos,id=id)
    pedi.delete()
    messages.success(request, "Eliminacion Pedido OK!!") 
    return redirect(to="pedidos/listarPedidos.html")










def buscar_articulos(request):
   # if request.GET['descripcion']:
   #     descripbusqueda = request.GET['descripcion']
   #     resultado = Articulos.objects.filter(Descripcion_icontains = descripbusqueda)
   #     return render (request, "resultado_buscararticulo.html", {"resultado" : descripbusqueda})
   # else:
   #     return HttpResponse ("campo vacio")
   # return HttpResponse (f"estamos buscando articulos con {request.GET['descripcion']}")
    #return render(request,  "buscar_articulo.html")
    return render(request, "articulos/buscar_articulo.html")

'''
def alta_clientes(request):
    if request.method == 'POST':
        mi_formulario = AbmCliente_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            #return  HttpResponse ( datos )
            ##cliente = Clientes(Cuit = request.POST['Cuit'], RSocial=request.POST['RSocial'], Domicilio=request.POST['Domi'], Mail=request.POST['Mail'], Telefono=request.POST['Tele'] ,Activo=xactivo )
            cliente = Clientes( Cuit = datos['cuit'], RSocial=datos['rsocial'], Domicilio=datos['domicilio'],Mail=datos['mail'],Telefono=datos['telefono'], Activo = datos['activo'] )
            cliente.save()
            textoresultado ="El registro fue grabado OK!!"  
            return  HttpResponse(textoresultado)
        else:
            textodeerror ="Is Valid false"  
            return  HttpResponse(textodeerror)
            #return render(request, "abmclientes.html")
    return render(request="abmclientes.html")   
        
def abm_articulos(request):
    return render(request, "abmArticulo.html")




def alta_articulos(request):
    if request.method == 'POST':
        mi_formulario = AbmArticulo_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            articulo = Articulos( Codigo = datos['codigo'], Descripcion=datos['descrip'], UnidadMedida=datos['um'],Precio=datos['puni'] )
            articulo.save()
            textoresultado ="El registro fue grabado OK!!"  
            return  HttpResponse(textoresultado)
        else:
            textodeerror ="Is Valid false"  
            return  HttpResponse(textodeerror)
            #return render(request, "abmclientes.html")
    return render(request="abmArticulo.html")




def abm_pedidos(request):
    return render(request, "abmpedidos.html")


@login_required( login_url="/AppUsuario/Login" )
def alta_pedido(request):
    if request.method == 'POST':
        mi_formulario = AbmPedido_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            #print (datos)
            pedido =  Pedidos( NroPedido = datos['nropedido'], Fecha=datos['fecha'], CuitCliente=datos['cuit'],Importe=datos['importe'] )
            pedido.save()
            textoresultado ="El registro de pedidofue grabado OK!!"  
            return  HttpResponse(textoresultado)
        else:
            textodeerror ="Is Valid false"  
            return  HttpResponse(textodeerror)
            #return render(request, "abmclientes.html")
    return render(request="abmArticulo.html")




'''

 
    




