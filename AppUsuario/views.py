from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from AppUsuario.forms import UserEditForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppUsuario.models import Avatar


# Create your views here.


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            print(usuario)
            contra=form.cleaned_data.get("password")  
            
            user= authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request, "inicio.html", {"url":avatares[0].imagen.url} ) #, {"mensaje":f"Bienvenido {usuario}"})
            else:
                return HttpResponse("usuario incorrecto")
        else:
            #return HttpResponse(f"No se pudo validar el login {form}")
            return redirect(to="Login")
        
    form = AuthenticationForm()
    return render(request , "login.html", {"form":form})
         


         


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("usuario creado")
    else:
        
        form = UserCreationForm()
    return render(request, "registro.html", {"form":form})
    
            


@login_required
def editarPerfil(request):
    
    usuario= request.user
    
    if request.method == "POST":
        
        miFormulario=UserEditForm(request.POST)
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email =informacion['email']
            
            password = informacion['password1']
            
            usuario.set_password(password)
            
            usuario.save()
            
            return render(request, "inicio.html")
        
        
    else:
    
        miFormulario=UserEditForm(initial={'email':usuario.email})
        
    return render(request, "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})

      