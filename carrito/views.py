from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from carrito.models import Producto
from carrito.carrito import carrito  


## vista para el catalogo 
def catalogo(request):

    productos = Producto.objects.all()
    total_carrito = 0
    
    if "carrito" in request.session:

        for item in request.session["carrito"].values():
            total_carrito += item["acumulado"] 

    return render(request, 'catalogo.html', {"productos": productos, "total_carrito": total_carrito})


## pedimos login para agregar productos
@login_required
def agregar_producto(request, producto_id):

    mi_carrito = carrito(request)  
    producto = Producto.objects.get(id=producto_id)

    mi_carrito.agregar(producto)
    
    return redirect("catalogo")

def eliminar_producto(request, producto_id):
    mi_carrito = carrito(request)
    producto = Producto.objects.get(id=producto_id)
    mi_carrito.eliminar(producto)

    return redirect("catalogo")

def restar_producto(request, producto_id):
    mi_carrito = carrito(request)
    producto = Producto.objects.get(id=producto_id)
    mi_carrito.restar(producto)

    return redirect("catalogo")

def limpiar_carrito(request):
    mi_carrito = carrito(request)
    mi_carrito.limpiar()

    return redirect("catalogo")



from .models import Orden, OrdenProducto
from django.contrib import messages

@login_required
def guardar_orden(request):
    carrito = request.session.get('carrito', {})

    if carrito:
        ## crear una nueva orden
        orden = Orden.objects.create(
            usuario=request.user,
            total=sum(item['acumulado'] for item in carrito.values())
        )

        ## guardar los productos de la orden
        for item in carrito.values():
            producto = Producto.objects.get(id=item['producto_id'])
            OrdenProducto.objects.create(
                orden=orden,
                producto=producto,
                cantidad=item['cantidad']
            )

        ## limpiar el carrito
        request.session['carrito'] = {}
        messages.success(request, '¡Tu orden ha sido guardada exitosamente!')
        return redirect('catalogo')
    
    else:
        return redirect('catalogo')