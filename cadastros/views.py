from django.http import HttpResponse
from django.shortcuts import render, redirect

from usuarios.models import Usuario
from .forms import CategoriaForm
from .models import Categorias, Produtos, Servicos


def clientes(request):
    if request.session.get('usuario'):
        return HttpResponse('Ola')
    else:
        return redirect('/login/?status=2')


def categorias(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        categoria = Categorias.objects.order_by('-id')
        return render(request, 'categorias.html',
                      {'categoria': categoria, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')


def criar_categoria(request):
    id_usuario = request.session.get('usuario')

    if id_usuario:
        form = CategoriaForm()

        if request.method == 'POST':
            form = CategoriaForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect('/categorias/')

        contexto = {'usuario_logado': id_usuario, 'form': form}
        return render(request, 'cria_categoria.html', context=contexto)

    return redirect('/login/?status=2')


def edita_categoria(request, id):
    if request.session.get('usuario'):
        categoria = Categorias.objects.get(id=id)
        if request.method == 'POST':
            descricao = request.POST.get('descricao')
            produto = request.POST.get('produto')
            servico = request.POST.get('servico')
            if produto:
                produto = True
            else:
                produto = False

            if servico:
                servico = True
            else:
                servico = False

            categoria.descricao = descricao
            categoria.produto = produto
            categoria.servico = servico
            categoria.save()
            return redirect('/categorias')
        return render(request, 'edita_categoria.html',
                      {'categoria': categoria, 'usuario_logado': request.session.get('usuario')})


def excluir_categoria(request, id):
    categoria = Categorias.objects.get(id=id).delete()
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
        return render(request, 'cria_produto.html',
                      {'categorias': categorias, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')


def valida_produto(request):
    descricao = request.POST.get('descricao')
    preco_venda = request.POST.get('preco_venda')
    quantidade = request.POST.get('quantidade')
    categoria = request.POST.get('categoria')
    observacao = request.POST.get('observacao')
    try:
        cat = Categorias.objects.get(descricao=categoria)
        produto = Produtos(descricao=descricao, preco_venda=preco_venda, quantidade=quantidade,
                           categoria=cat, observacao=observacao)
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
        categorias = Categorias.objects.filter(servico=True)
        return render(request, 'cria_servico.html',
                      {'categorias': categorias, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')


def valida_servico(request):
    descricao = request.POST.get('descricao')
    valor = request.POST.get('valor')
    observacao = request.POST.get('observacao')
    categoria = request.POST.get('categoria')

    # cat = Categorias.objects.get(descricao = categoria)

    servico = Servicos(descricao=descricao, valor=valor,
                       observacao=observacao, categoria_id=categoria)
    servico.save()

    return redirect('/servicos')


def edita_produto(request, id):
    if request.session.get('usuario'):
        produto = Produtos.objects.get(id=id)
        categorias = Categorias.objects.filter(produto=True)
        if request.method == 'POST':
            descricao = request.POST.get('descricao')
            preco_venda = request.POST.get('preco_venda')
            quantidade = request.POST.get('quantidade')
            categoria = request.POST.get('categoria')
            observacao = request.POST.get('observacao')

            produto.descricao = descricao
            produto.preco_venda = preco_venda
            produto.quantidade = quantidade
            produto.categoria_id = categoria
            produto.observacao = observacao
            produto.save()
            return redirect('/produtos')
        contexto = {'produto': produto, 'categorias': categorias, 'usuario_logado': request.session.get('usuario')}
        return render(request, 'edita_produto.html', contexto)


def edita_servico(request, id):
    if request.session.get('usuario'):
        servico = Servicos.objects.get(id=id)
        categorias = Categorias.objects.filter(servico=True)
        if request.method == 'POST':
            descricao = request.POST.get('descricao')
            valor = request.POST.get('valor')
            categoria = request.POST.get('categoria')
            observacao = request.POST.get('observacao')
            try:
                servico.descricao = descricao
                servico.valor = valor
                servico.categoria_id = categoria
                servico.observacao = observacao
                servico.save()
            except:
                return HttpResponse('Erro')
            return redirect('/servicos')
        return render(request, 'edita_servico.html', {'servico': servico, 'categorias': categorias,
                                                      'usuario_logado': request.session.get('usuario')})


def excluir_produto(request, id):
    produto = Produtos.objects.get(id=id).delete()
    return redirect('/produtos')


def excluir_servico(request, id):
    servico = Servicos.objects.get(id=id).delete()
    return redirect('/servicos')


def busca_cat(request):
    if request.session.get('usuario'):
        categoria = Categorias.objects.order_by('-id')
        return render(request, '/bsuca_cat.html',
                      {'categoria': categoria, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')


def terceiros(request):
    pass

