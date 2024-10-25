
from django.contrib import admin
from django.urls import path, include
from carrito.views import *

urlpatterns = [

    ## url admin
    path('admin/', admin.site.urls),
    
    ## url para core
    path('',include('core.urls')),

    ## url para login  y catalogo
    path('accounts/', include('django.contrib.auth.urls')),
    path('catalogo/', catalogo, name='catalogo'),

    ## url para carrito     
    path('agregar/<int:producto_id>',agregar_producto,name="add"),
    path('eliminar/<int:producto_id>',eliminar_producto,name="del"),
    path('restar/<int:producto_id>',restar_producto,name="sub"),
    path('limpiar/',limpiar_carrito,name="cls"),
    path('guardar-orden/', guardar_orden, name='guardar_orden'),
]


## exclusivo para soportar imagenes

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
