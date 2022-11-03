from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Categorias, Produtos, Servicos
from django.core.paginator import Paginator


def clientes(request):
    if request.session.get('usuario'):
        return HttpResponse('Ola')
    else:
        return redirect('/login/?status=2')


def categorias(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        categoria = Categorias.objects.order_by('-id')

        paginator = Paginator(categoria, 10)
        page = request.GET.get('p')
        categoria = paginator.get_page(page)

        return render(request, 'categorias.html', {'categoria': categoria, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')

def cria_categoria(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        return render(request, 'cria_categoria.html', {'usuario_logado': request.session.get('usuario')})
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
    return render(request, 'edita_categoria.html', {'categoria': categoria, 'usuario_logado': request.session.get('usuario')})

def excluir_categoria(request, id):
    categoria = Categorias.objects.get(id = id).delete()
    return redirect('/categorias')

def produtos(request):
    if request.session.get('usuario'):
        produto = Produtos.objects.order_by('-id')
        return render(request, 'produtos.html', {'produtos': produto, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')


def cria_produto(request):
    if request.session.get('usuario'):
        categorias = Categorias.objects.all()
        return render(request, 'cria_produto.html', {'categorias': categorias, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')


def valida_produto(request):
    descricao = request.POST.get('descricao')
    preco_venda = request.POST.get('preco_venda')
    quantidade = request.POST.get('quantidade')
    categoria = request.POST.get('categoria')
    observacao = request.POST.get('observacao')
    try:
        cat = Categorias.objects.get(descricao = categoria)
        produto = Produtos(descricao = descricao, preco_venda = preco_venda, quantidade = quantidade,
                           categoria = cat, observacao = observacao)
        produto.save()
        return redirect('/produtos/')
    except:
        return HttpResponse('Falha no cadastro')


def servicos(request):
    if request.session.get('usuario'):
        servico = Servicos.objects.order_by('-id')
        return render(request, 'servicos.html', {'servicos': servico, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')


def cria_servico(request):
    if request.session.get('usuario'):
        categorias = Categorias.objects.all()
        return render(request, 'cria_servico.html', {'categorias': categorias, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')


def valida_servico(request):
    descricao = request.POST.get('descricao')
    valor = request.POST.get('valor')
    observacao = request.POST.get('observacao')
    categoria = request.POST.get('categoria')

    #cat = Categorias.objects.get(descricao = categoria)

    servico = Servicos(descricao = descricao, valor = valor,
                       observacao = observacao, categoria_id = categoria)
    servico.save()

    return redirect('/servicos')