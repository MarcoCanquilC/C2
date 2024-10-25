
from django.urls import path
from .views import inicio,formulario,salir,register

urlpatterns = [

    ## url para templates 
    
    path('', inicio, name= 'inicio'),
    path('formulario/', formulario, name= 'formulario'),
    path('logout/',salir,name='salir'),
    path('register/',register,name='register'),
   
]



