from django.shortcuts import render
from website.models import Pessoa, Ideia
# Create your views here.

def index(request):
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.save()
        contexto = {'msg':'usuario cadastrado'}
    return render(request,'index.html', contexto)

def sobre(request):
    # essa pagina listara ideias e seus criadoes
    contexto = {
        'pessoas':pessoa
    }
    return render(request, 'sobre.html', contexto)


