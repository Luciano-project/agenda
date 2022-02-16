from django.shortcuts import render, HttpResponse, redirect
from .models import Evento

# Create your views here.

def index(request):
    return redirect('/agenda/')

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





# Classe para exibir o nome de determinado evento:
#def evento_django(request,none):
    #evedj=Evento.titulo
    #return HttpResponse(none)
