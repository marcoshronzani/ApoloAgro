from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.exceptions import ValidationError

from usuarios.models import Usuario
from .forms import CategoriaForm, ClienteForm, TerceiroForm, UndMedidaForm
from .models import Categorias, Produtos, Servicos, Clientes, Terceiros, UnidadeMedida


def categorias(request):
    if request.session.get('usuario'):
        termo = request.GET.get('termo')
        if termo:
            categoria = Categorias.objects.order_by('-id').filter(descricao__icontains=termo)
        else:
            categoria = Categorias.objects.order_by('-id')

        param_pagina = request.GET.get('pagina', '1')
        param_limite = request.GET.get('limite', '10')

        if not (param_limite.isdigit() and int(param_limite) > 0):
            param_limite = '10'

        cat_paginator = Paginator(categoria, param_limite)
        try:
            pagina = cat_paginator.page(param_pagina)
        except:
            pagina = cat_paginator.page(1)
        
        contexto = {'categoria': pagina, 'usuario_logado': request.session.get('usuario'), 
                    'opcoes_qnt_por_pagina': ['10', '30', '50', '100'], 'qnt_por_pagina': param_limite }

        return render(request, 'categorias.html', context=contexto)

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
        termo = request.GET.get('termo')

        if termo:
            produto = Produtos.objects.order_by('-id').filter(descricao__icontains=termo)
        else:
            produto = Produtos.objects.order_by('-id')
        
        param_pagina = request.GET.get('pagina', '1')
        param_limite = request.GET.get('limite', '10')

        if not (param_limite.isdigit() and int(param_limite) > 0):
            param_limite = '10'

        prd_paginator = Paginator(produto, param_limite)
        try:
            pagina = prd_paginator.page(param_pagina)
        except:
            pagina = prd_paginator.page(1)

        return render(request, 'produtos.html', {'produtos': pagina, 'usuario_logado': request.session.get('usuario'),
                                                    'opcoes_qnt_por_pagina': ['10', '30', '50', '100'], 'qnt_por_pagina': param_limite})
    else:
        return redirect('/login/?status=2')


def cria_produto(request):
    if request.session.get('usuario'):
        categorias = Categorias.objects.filter(produto=True)
        und_medidas = UnidadeMedida.objects.all()
        return render(request, 'cria_produto.html',
                      {'categorias': categorias, 'usuario_logado': request.session.get('usuario'),
                        'und_medidas':und_medidas})
    else:
        return redirect('/login/?status=2')


def valida_produto(request):
    descricao = request.POST.get('descricao')
    preco_venda = request.POST.get('preco_venda')
    quantidade = request.POST.get('quantidade')
    categoria = request.POST.get('categoria')
    observacao = request.POST.get('observacao')
    und_medida = request.POST.get('und_medida')
    try:
        cat = Categorias.objects.get(descricao=categoria)
        und_m = UnidadeMedida.objects.get(sigla=und_medida)
        produto = Produtos(descricao=descricao, preco_venda=preco_venda, quantidade=quantidade,
                           categoria=cat, observacao=observacao, und=und_m)
        produto.save()
        return redirect('/produtos/')
    except:
        return HttpResponse('Falha no cadastro')


def servicos(request):
    if request.session.get('usuario'):
        termo = request.GET.get('termo')

        if termo:
            servico = Servicos.objects.order_by('-id').filter(descricao__icontains=termo)
        else:
            servico = Servicos.objects.order_by('-id')
        
        param_pagina = request.GET.get('pagina', '1')
        param_limite = request.GET.get('limite', '10')

        if not (param_limite.isdigit() and int(param_limite) > 0):
            param_limite = '10'

        srv_paginator = Paginator(servico, param_limite)
        try:
            pagina = srv_paginator.page(param_pagina)
        except:
            pagina = srv_paginator.page(1)

        return render(request, 'servicos.html', {'servicos': pagina, 'usuario_logado': request.session.get('usuario'),
                                                    'opcoes_qnt_por_pagina': ['10', '30', '50', '100'], 'qnt_por_pagina': param_limite})
    else:
        return redirect('/login/?status=2')


def cria_servico(request):
    if request.session.get('usuario'):
        categorias = Categorias.objects.filter(servico=True)
        und_medidas = UnidadeMedida.objects.all()
        return render(request, 'cria_servico.html',
                      {'categorias': categorias, 'und_medidas': und_medidas, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')


def valida_servico(request):
    descricao = request.POST.get('descricao')
    valor = request.POST.get('valor')
    observacao = request.POST.get('observacao')
    categoria = request.POST.get('categoria')
    und_medida = request.POST.get('und_medida')

    # cat = Categorias.objects.get(descricao = categoria)

    servico = Servicos(descricao=descricao, valor=valor,
                       observacao=observacao, categoria_id=categoria, und_id=und_medida)

    servico.save()

    return redirect('/servicos')


def edita_produto(request, id):
    if request.session.get('usuario'):
        produto = Produtos.objects.get(id=id)
        categorias = Categorias.objects.filter(produto=True)
        und_medidas = UnidadeMedida.objects.all()
        if request.method == 'POST':
            descricao = request.POST.get('descricao')
            preco_venda = request.POST.get('preco_venda')
            quantidade = request.POST.get('quantidade')
            categoria = request.POST.get('categoria')
            observacao = request.POST.get('observacao')
            und_medida = request.POST.get('und_medida')

            produto.descricao = descricao
            produto.preco_venda = preco_venda
            produto.quantidade = quantidade
            produto.categoria_id = categoria
            produto.observacao = observacao
            produto.und_id = und_medida

            produto.save()
            return redirect('/produtos')
        contexto = {'produto': produto, 'categorias': categorias, 'usuario_logado': request.session.get('usuario'),
                    'und_medidas':und_medidas}
        return render(request, 'edita_produto.html', contexto)


def edita_servico(request, id):
    if request.session.get('usuario'):
        servico = Servicos.objects.get(id=id)
        categorias = Categorias.objects.filter(servico=True)
        und_medidas = UnidadeMedida.objects.all()
        if request.method == 'POST':
            descricao = request.POST.get('descricao')
            valor = request.POST.get('valor')
            categoria = request.POST.get('categoria')
            observacao = request.POST.get('observacao')
            und_medida = request.POST.get('und_medida')
            try:
                servico.descricao = descricao
                servico.valor = valor
                servico.categoria_id = categoria
                servico.observacao = observacao
                servico.und_id = und_medida
                servico.save()
            except:
                return HttpResponse('Erro')
            return redirect('/servicos')
        return render(request, 'edita_servico.html', {'servico': servico, 'categorias': categorias,
                                                      'usuario_logado': request.session.get('usuario'),
                                                      'und_medidas': und_medidas})


def excluir_produto(request, id):
    Produtos.objects.get(id=id).delete()
    return redirect('/produtos')


def excluir_servico(request, id):
    Servicos.objects.get(id=id).delete()
    return redirect('/servicos')


def busca_cat(request):
    if request.session.get('usuario'):
        categoria = Categorias.objects.order_by('-id')
        return render(request, '/bsuca_cat.html',
                      {'categoria': categoria, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/login/?status=2')


def clientes(request):
    if request.session.get('usuario'):
        termo = request.GET.get('termo')

        if termo:
            clientes = Clientes.objects.order_by('-id').filter(Q(razao_social__icontains=termo) | 
                                                                Q(cnpj__icontains=termo) |
                                                                Q(cpf__icontains=termo))
        else:
            clientes = Clientes.objects.order_by('-id')

        param_pagina = request.GET.get('pagina', '1')
        param_limite = request.GET.get('limite', '10')

        if not (param_limite.isdigit() and int(param_limite) > 0):
            param_limite = '10'
        
        cli_paginator = Paginator(clientes, param_limite)
        try:
            pagina = cli_paginator.page(param_pagina)
        except:
            pagina = cli_paginator.page(1)

        contexto = {'clientes': pagina, 'usuario_logado': request.session.get('usuario'),
                    'opcoes_qnt_por_pagina': ['10', '30', '50', '100'], 'qnt_por_pagina': param_limite}

        return render(request, 'clientes.html', context=contexto)
    
    return redirect('/login/?status=2')

def cria_cliente(request):
    if request.session.get('usuario'):

        form = ClienteForm()

        if request.method == 'POST':
            form = ClienteForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect('/clientes/')
            
        contexto = {'usuario_logado': request.session.get('usuario'), 'form': form}
        return render(request, 'cria_cliente.html', context=contexto)

    return redirect('/login/?status=2')


def excluir_cliente(request, id):
    Clientes.objects.get(id=id).delete()
    return redirect('/clientes')


def edita_cliente(request, id):
    if request.session.get('usuario'):
        cliente = Clientes.objects.get(id=id)
        form = ClienteForm(instance=cliente)

        if request.method == 'POST':
            form = ClienteForm(request.POST, instance=cliente)

            if form.is_valid():
                form.save()

                return redirect('/clientes/')

        contexto = {'usuario_logado':request.session.get('usuario'), 'form': form, 'cliente':cliente}
        return render(request, 'edita_cliente.html', context=contexto)

    return redirect('/login/?status=2')


def terceiros(request):
    if request.session.get('usuario'):
        termo = request.GET.get('termo')

        if termo:
            terceiros = Terceiros.objects.order_by('-id').filter(Q(razao_social__icontains=termo) | 
                                                                    Q(cnpj__icontains=termo) |
                                                                    Q(cpf__icontains=termo))
        else:
            terceiros = Terceiros.objects.order_by('-id')
        
        param_pagina = request.GET.get('pagina', '1')
        param_limite = request.GET.get('limite', '10')

        if not (param_limite.isdigit() and int(param_limite) > 0):
            param_limite = '10'
        
        ter_paginator = Paginator(terceiros, param_limite)
        try:
            pagina = ter_paginator.page(param_pagina)
        except:
            pagina = ter_paginator.page(1)
        return render(request, 'terceiros.html', {'terceiros': pagina, 'usuario_logado': request.session.get('usuario'),
                                                    'opcoes_qnt_por_pagina': ['10', '30', '50', '100'], 'qnt_por_pagina': param_limite})

    return redirect('/login/?status=2')

def cria_terceiro(request):
    if request.session.get('usuario'):
        form = TerceiroForm()

        if request.method == 'POST':
            form = TerceiroForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect('/terceiros/')

        contexto = {'usuario_logado': request.session.get('usuario'), 'form': form}
        return render(request, 'cria_terceiro.html', context=contexto)

    return redirect('/login/?status=2')


def edita_terceiro(request, id):
    if request.session.get('usuario'):
        terceiro = Terceiros.objects.get(id=id)
        form = TerceiroForm(instance=terceiro)

        if request.method == 'POST':
            form = ClienteForm(request.POST, instance=terceiro)

            if form.is_valid():
                form.save()

                return redirect('/terceiros/')

        contexto = {'usuario_logado': request.session.get('usuario'), 'form': form, 'terceiro': terceiro}
        return render(request, 'edita_terceiro.html', context=contexto)
    
    return redirect('/login/?status=2')


def excluir_terceiro(request, id):
    Terceiros.objects.get(id=id).delete()
    return redirect('/terceiros/')


def unidade_medida(request):
    if request.session.get('usuario'):
        termo = request.GET.get('termo')

        if termo:
            und_medidas = UnidadeMedida.objects.order_by('-id').filter(descricao__icontains=termo)
        else:
            und_medidas = UnidadeMedida.objects.order_by('-id')

        return render(request, 'und_medidas.html', {'und_medidas': und_medidas, 'usuario_logado': request.session.get('usuario')})
    
    return redirect('/login/?status=2')


def cria_und_medida(request):
    if request.session.get('usuario'):
        form = UndMedidaForm()

        if request.method =='POST':
            form = UndMedidaForm(request.POST)

            if form.is_valid():
                form.save()
            
                return redirect('/unidade_medida/')

        contexto = {'usuario_logado': request.session.get('usuario'), 'form': form}
        return render(request, 'cria_und_medida.html', context=contexto)
    
    return redirect('/login/?status=2')


def edita_und_medida(request, id):
    if request.session.get('usuario'):
        und = UnidadeMedida.objects.get(id=id)
        form = UndMedidaForm(instance=und)
        
        if request.method == 'POST':
            form = UndMedidaForm(request.POST, instance=und)
            if form.is_valid():
                form.save()

                return redirect('/unidade_medida/')

        contexto = {'usuario_logado': request.session.get('usuario'), 'form': form, 'und': und}
        return render(request, 'edita_und_medidas.html', context=contexto)
        
    return redirect('/login/?status=2')


def excluir_und_medida(request, id):
    UnidadeMedida.objects.get(id=id).delete()
    return redirect('/unidade_medida')