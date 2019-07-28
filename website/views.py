from django.shortcuts import render,redirect
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
        return render(request,'login.html', contexto)
    return render(request,'index.html', contexto)

def sobre(request):
    # essa pagina listara ideias e seus criadoes
    ideias = Ideia.objects.all()
    contexto = {
        'ideias':ideias
    }
    return render(request, 'sobre.html', contexto)


def login(request):

    contexto = {

    }
    if request.method == 'POST':
        email_form = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email= email_form).first()
        if pessoa is None:
            contexto = {'msg':'Cadastre-se para criar uma ideia'}
            return render(request, 'index.html', contexto)
        else:
            #mandar para página de ideias
            contexto = {'pessoa': pessoa}
            return render(request, 'ideias.html', contexto)
   
    return render(request, 'login.html', contexto)

def cadastrar_ideia(request):
    contexto = {

    }
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email = email_pessoa).first()
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categorias = request.POST.get('categoria')
            ideia.caregorias = request.POST.get('caregorias_outros')
            ideia.save()
            redirect('/sobre')
    return render(request, 'ideias.html', contexto)