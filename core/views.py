from django.shortcuts import render, HttpResponse, redirect
from .models import Evento

# Para podermos permitir o acesso somente de pessoas autenticadas
from django.contrib.auth.decorators import login_required

# ** aqui estão importações relacionadas a autentificações e serão usadas adiante
from django.contrib.auth import authenticate, login, logout


# Caso negativo do segundo if
from django.contrib import messages
# Create your views here.

# def index(request):
#    return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

# Aqui vamos recuperar os itens dos formulários que temos no html
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Antes de continuar aqui precisam ser importadas bibliotecas **
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")

    return redirect('/')

@login_required(login_url= '/login/')
#aqui estamos criando a função que irá listar os eventos
def lista_eventos(request):
    #primeiro extraímos o objeto (do id=1) de Evento para evento
    #evento = Evento.objects.get(id=1)

    #evento = Evento.objects.all()

    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)

    #Estamos passando os dados dos objetos para um dicionário, dicionário esse que será usado para listar os eventos no template
    dados= {'eventos':evento}
    return render(request,'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    return render(request,'evento.html')

# Usando a verificação de login
@login_required(login_url='/login/')
# aqui vamos buscar os dados que foram inseridos para mandá-los ao banco de dados
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                             data_evento=data_evento,
                             descricao=descricao,
                             usuario=usuario)
    return redirect('/')
# Classe para exibir o nome de determinado evento:
#def evento_django(request,none):
    #evedj=Evento.titulo
    #return HttpResponse(none)
