from django.shortcuts import render, redirect, HttpResponse
from tela.forms import form_login
from tela.forms import form_cadastro
from django.contrib.auth.models import User
from django.contrib.auth import models,authenticate
from .models import banco_de_login


def tela_login(request): #LOGIN E AUTENTIFICAÇÃO
    form = form_login()

    if request.method == 'GET':
    
        return render (request,"html/main_tela.html", {'login':form})

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['senha']

        user = banco_de_login.objects.filter(username=username).first()

        if user:
            return redirect ('usuario_logado')
            
        else:
            return redirect ('erro_')
 

def tela_cadastro(request): #CADASTRO DE USUARIO

    if request.method == 'GET':   
        form = form_cadastro()
        return render(request, "html/main_cadastro.html", {'cadastro':form })
       

    form = form_cadastro(request.POST or None)

    if request.method == 'POST':

        form_ = form_cadastro(request.POST)

        if request.POST:
            if form.is_valid(): 
                form.save()
                return redirect ('login_page')

def usuario_logado(request): # tela de logado com sucesso
    return render (request, "html/user_sucess.html")

def erro_register(request): #erro de usuario nao cadastrado
        return render (request, 'html/erro/user_cadas_no.html')

