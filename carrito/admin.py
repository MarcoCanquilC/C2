from django.contrib import admin
from carrito.models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio')


## creamos para editar ordenes
from carrito.models import Orden, OrdenProducto

class OrdenProductoInline(admin.TabularInline):
    model = OrdenProducto
    extra = 1

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total', 'estado', 'fecha')  
    list_filter = ('estado', 'fecha')  ## filtros
    inlines = [OrdenProductoInline]  

admin.site.register(Orden, OrdenAdmin)