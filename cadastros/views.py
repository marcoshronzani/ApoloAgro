from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Categorias
from django.core.paginator import Paginator


def clientes(request):
    if request.session.get('usuario'):
        return HttpResponse('Ola')
    else:
        return redirect('/login/?status=2')


def categorias(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        categoria = Categorias.objects.all()

        paginator = Paginator(categoria, 5)
        page = request.GET.get('p')
        categoria = paginator.get_page(page)

        return render(request, 'categorias.html', {'categoria': categoria})
    else:
        return redirect('/login/?status=2')

def cria_categoria(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        return render(request, 'cria_categoria.html')
    else:
        return redirect('/login/?status=2')

def valida_categoria(request):
    descricao = request.POST.get('descricao')
    produto = request.POST.get('produto')
    servico = request.POST.get('servico')
    if produto:
        produto = 1
    else:
        produto = 0

    if servico:
        servico = 1
    else:
        servico = 0

    try:
        categoria = Categorias(descricao = descricao,
                               produto = produto,
                               servico = servico)
        categoria.save()
        return redirect('/categorias/')
    except:
        return HttpResponse('Falhou')

def edita_categoria(request, id):
    categoria = Categorias.objects.get(id = id)
    return render(request, 'edita_categoria.html', {'categoria': categoria})

def excluir_categoria(request, id):
    categoria = Categorias.objects.get(id = id).delete()
    return redirect('/categorias')