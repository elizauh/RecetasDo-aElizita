from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from apps.recetas.models import Receta
from .validacoes import *
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create(request):
    if request.method == 'POST':
        nombre                  = request.POST['nombre']
        email                 = request.POST['email']
        password              = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        erros = 0
        if campo_vazio(nombre):
            messages.error(request, 'Campo obligatorio!')
            erros += 1
        if campo_vazio(email):
            messages.error(request, 'Campo obligatorio!')
            erros += 1
        if usuario_cadastrado(nombre, email):
            messages.error(request, 'Usuario ya esta registrado!')
            erros += 1
        if campo_vazio(password):
            messages.error(request, 'Campo obligatorio!')
            erros += 1
        if senhas_diferentes(password, password_confirmation):
            messages.error(request, 'Las claves deben ser iguales!')
            erros += 1
        if erros > 0:
            return redirect('registro')
        
        user = User.objects.create_user(username=nombre, email=email, password=password)
        user.save()

        ## Minimos privilegios
        usuarios, created = Group.objects.get_or_create(name='usuarios')        
        ct = ContentType.objects.get_for_model(Receta)

        
        permission = Permission.objects.create(codename='can_add_receta',
                                        name='Can add receta',
                                        content_type=ct)

        permission2 = Permission.objects.create(codename='can_change_receta',
                                        name='Can change receta',
                                        content_type=ct)
        permission3 = Permission.objects.create(codename='can_delete_receta',
                                        name='Can delete receta',
                                        content_type=ct)
        permission4 = Permission.objects.create(codename='can_view_receta',
                                        name='Can view receta',
                                        content_type=ct)
        usuarios.permissions.add(permission)
        usuarios.permissions.add(permission2)
        usuarios.permissions.add(permission3)
        usuarios.permissions.add(permission4)

        user.groups.add(usuarios)
        ##
        
        messages.success(request, f"Usuario {user.username} registrado con exito!")

        return redirect('usuarios.login')
    
    return render(request, 'usuarios/registro.html')

def login(request):
    if request.method == 'POST':
        email    = request.POST['email']
        password = request.POST['password']
        
        if campo_vazio(email) or campo_vazio(password):
            messages.error(request, 'Todos los campos son obligatorios!')
            return redirect('usuarios.login')
    
        if User.objects.filter(email=email).exists():
            nombre = User.objects.filter(email=email).values_list('username', flat=True).first()
            user = auth.authenticate(request=request, username=nombre, password=password)
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Inicio de sesion realizado con exito!')
                
                return redirect('usuarios.dashboard')
        
    return render(request, 'usuarios/login.html')


""" def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Inicie sesion para acceder a la pagina \'Mis recetas\'!')
        return redirect('usuarios.login')
    
    recetas = Receta.objects.filter(persona=request.user.id).order_by('data_criacao')
    
    return render(request, 'usuarios/dashboard.html', {'recetas': recetas})
 """

#cumple la misma función
@login_required
def dashboard(request):        
    recetas = Receta.objects.filter(persona=request.user.id).order_by('data_criacao')    
    return render(request, 'usuarios/dashboard.html', {'recetas': recetas})

def logout(request):
    auth.logout(request)
    return redirect('recetas.index')
