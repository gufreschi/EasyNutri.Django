from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Paciente

def role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        request.session['role'] = role
        if role == 'nutri':
            return redirect('cadastro-nutri')
        elif role == 'paciente':
            return redirect('cadastro-paciente')

    return render(request, 'role.html')

def sobre(request):
    return render(request, 'sobre.html')

########## PACIENTE ##########

def home_paciente(request):
    return render(request, 'paciente/home.html', {})

def register_paciente(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        # data_nascimento = request.POST.get('data_nascimento')
        # telefone = request.POST.get('telefone')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')
        
        user = User.objects.filter(username=username).first()
        if user:
            messages.error(request, ('Esse nome de usuário já existe'))
            return redirect('cadastro-paciente')
        
        if senha1 == senha2:
            user = User.objects.create_user(username=username, email=email, password=senha1)
            user.save()
            messages.success(request, ('Cadastro realizado com sucesso!'))
            return redirect('login-paciente')
        else:
            messages.error(request, ('As senhas devem ser iguais.'))
            return redirect('cadastro-paciente')
    else:
        return render(request, 'paciente/cadastro.html')

def login_paciente(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha1 = request.POST['senha1']
        user = authenticate(request, username=username, password=senha1)
        if user is not None:
            login(request, user)
            messages.success(request, ('Você está conectado!'))
            return redirect('home-paciente')
        else:
            messages.error(request, ('Aconteceu algum erro. Tente novamente...'))
            return redirect('login-paciente')

    else:
        return render(request, 'paciente/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('Você foi desconectado...'))
    return redirect('role')

########## NUTRICIONISTA ##########

def home_nutri(request):
    return render(request, 'nutri/home.html')

def registro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')

        cpf_check = Paciente.objects.filter(cpf=cpf).first()
        if cpf_check:
            messages.error(request, ('Esse cpf já está cadastrado'))
            return redirect('registro-de-pacientes')

        novo_paciente = Paciente(nome=nome, cpf=cpf, data_nascimento=data_nascimento)
        novo_paciente.save()
        return redirect('listagem-de-pacientes')
        
    return render(request, 'nutri/registro.html',)

def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'nutri/pacientes.html', {'pacientes': pacientes})

def register_nutri(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        # data_nascimento = request.POST.get('data_nascimento')
        # telefone = request.POST.get('telefone')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')
        
        user = User.objects.filter(username=username).first()
        if user:
            messages.error(request, ('Esse nome de usuário já existe'))
            return redirect('cadastro-nutri')
        
        if senha1 == senha2:
            user = User.objects.create_user(username=username, email=email, password=senha1)
            user.save()
            messages.success(request, ('Cadastro realizado com sucesso!'))
            return redirect('login-nutri')
        else:
            messages.error(request, ('As senhas devem ser iguais.'))
            return redirect('cadastro-nutri')
    else:
        return render(request, 'nutri/cadastro.html')

def login_nutri(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha1 = request.POST['senha1']
        user = authenticate(request, username=username, password=senha1)
        if user is not None:
            login(request, user)
            messages.success(request, ('Você está conectado!'))
            return redirect('home-nutri')
        else:
            messages.error(request, ('Aconteceu algum erro. Tente novamente...'))
            return redirect('login-nutri')

    else:
        return render(request, 'nutri/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('Você foi desconectado...'))
    return redirect('login-nutri')