from django.shortcuts import render, redirect
from tela.forms import form_login
from tela.forms import form_cadastro

def tela_login(request):

    form = form_login

    return render (request,"html/main_tela.html", {'login':form})

def tela_cadastro(request):

    form = form_cadastro(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect ('login_page')
            
    return render(request, "html/main_cadastro.html", {'cadastro':form })