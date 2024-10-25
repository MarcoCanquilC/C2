
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


from django.contrib.auth import logout,authenticate, login
from .forms import CustomedUserCreationForm


# Vistas para render
def inicio(request):
     
    if 'carrito' not in request.session:
        request.session['carrito'] = {}

    return render(request,'core/inicio.html')


def formulario(request):
    return render(request,'core/formulario.html')


def salir(request):
    logout(request)
    return redirect('inicio')


def register(request):

    if request.method == 'POST':
        form = CustomedUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
         
            login(request, user) 
            
            return redirect('inicio') 
    else:
        form = CustomedUserCreationForm()
       

    return render(request, 'registration/register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        ## autenticar al usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:

            ## inicia sesion
            login(request, user)
            return redirect('inicio') 
        
    
    return render(request, 'login.html')
