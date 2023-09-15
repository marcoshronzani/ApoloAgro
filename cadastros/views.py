from django.forms import inlineformset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib import messages


from usuarios.models import Usuario
from .forms import (
    CategoriaForm,
    ClienteForm,
    TerceiroForm,
    UndMedidaForm,
    ClienteEdtForm,
    TerceiroEdtForm,
    OrcamentoForm,
    ItemOrcaForm,
    ItemOrcaServForm,
)
from .models import (
    Categorias,
    Produtos,
    Servicos,
    Clientes,
    Terceiros,
    UnidadeMedida,
    Orcamentos,
    ItemOrcamento,
    ItemOrcamentoServico,
)


def categorias(request):
    if request.session.get("usuario"):
        termo = request.GET.get("termo")
        if termo:
            categoria = Categorias.objects.order_by("-id").filter(
                descricao__icontains=termo
            )
        else:
            categoria = Categorias.objects.order_by("-id")

        param_pagina = request.GET.get("pagina", "1")
        param_limite = request.GET.get("limite", "10")

        if not (param_limite.isdigit() and int(param_limite) > 0):
            param_limite = "10"

        cat_paginator = Paginator(categoria, param_limite)
        try:
            pagina = cat_paginator.page(param_pagina)
        except:
            pagina = cat_paginator.page(1)

        contexto = {
            "categoria": pagina,
            "usuario_logado": request.session.get("usuario"),
            "opcoes_qnt_por_pagina": ["10", "30", "50", "100"],
            "qnt_por_pagina": param_limite,
        }

        return render(request, "categorias.html", context=contexto)

    return redirect("/login/?status=2")


def criar_categoria(request):
    id_usuario = request.session.get("usuario")

    if id_usuario:
        form = CategoriaForm()

        if request.method == "POST":
            form = CategoriaForm(request.POST)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Cadastro Realizado!")

                return redirect("/categorias/")

        contexto = {"usuario_logado": id_usuario, "form": form}
        return render(request, "cria_categoria.html", context=contexto)

    return redirect("/login/?status=2")


def edita_categoria(request, id):
    if request.session.get("usuario"):
        categoria = Categorias.objects.get(id=id)
        if request.method == "POST":
            descricao = request.POST.get("descricao")
            produto = request.POST.get("produto")
            servico = request.POST.get("servico")
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
            messages.add_message(request, messages.SUCCESS, "Edição realizada!")
            return redirect("/categorias")
        return render(
            request,
            "edita_categoria.html",
            {"categoria": categoria, "usuario_logado": request.session.get("usuario")},
        )


def excluir_categoria(request, id):
    try:
        Categorias.objects.get(id=id).delete()
        messages.add_message(request, messages.SUCCESS, "Exclusão realizada!")
        return redirect("/categorias")
    except:
        messages.add_message(
            request,
            messages.ERROR,
            "Exclusão não permitida, Categoria em uso no sistema",
        )
        return redirect(f"/edita_categoria/{id}")


def produtos(request):
    if request.session.get("usuario"):
        termo = request.GET.get("termo")

        if termo:
            produto = Produtos.objects.order_by("-id").filter(
                descricao__icontains=termo
            )
        else:
            produto = Produtos.objects.order_by("-id")

        param_pagina = request.GET.get("pagina", "1")
        param_limite = request.GET.get("limite", "10")

        if not (param_limite.isdigit() and int(param_limite) > 0):
            param_limite = "10"

        prd_paginator = Paginator(produto, param_limite)
        try:
            pagina = prd_paginator.page(param_pagina)
        except:
            pagina = prd_paginator.page(1)

        return render(
            request,
            "produtos.html",
            {
                "produtos": pagina,
                "usuario_logado": request.session.get("usuario"),
                "opcoes_qnt_por_pagina": ["10", "30", "50", "100"],
                "qnt_por_pagina": param_limite,
            },
        )
    else:
        return redirect("/login/?status=2")


def cria_produto(request):
    if request.session.get("usuario"):
        categorias = Categorias.objects.filter(produto=True)
        und_medidas = UnidadeMedida.objects.all()
        return render(
            request,
            "cria_produto.html",
            {
                "categorias": categorias,
                "usuario_logado": request.session.get("usuario"),
                "und_medidas": und_medidas,
            },
        )
    else:
        return redirect("/login/?status=2")


def valida_produto(request):
    descricao = request.POST.get("descricao")
    preco_venda = request.POST.get("preco_venda")
    quantidade = request.POST.get("quantidade")
    categoria = request.POST.get("categoria")
    observacao = request.POST.get("observacao")
    und_medida = request.POST.get("und_medida")
    try:
        cat = Categorias.objects.get(descricao=categoria)
        und_m = UnidadeMedida.objects.get(sigla=und_medida)
        produto = Produtos(
            descricao=descricao,
            preco_venda=preco_venda,
            quantidade=quantidade,
            categoria=cat,
            observacao=observacao,
            und=und_m,
        )
        produto.save()
        messages.add_message(request, messages.SUCCESS, "Cadastro Realizado!")
        return redirect("/produtos/")
    except:
        messages.add_message(request, messages.ERROR, "Erro ao Validar Produto")
        return redirect("/produtos/")


def servicos(request):
    if request.session.get("usuario"):
        termo = request.GET.get("termo")

        if termo:
            servico = Servicos.objects.order_by("-id").filter(
                descricao__icontains=termo
            )
        else:
            servico = Servicos.objects.order_by("-id")

        param_pagina = request.GET.get("pagina", "1")
        param_limite = request.GET.get("limite", "10")

        if not (param_limite.isdigit() and int(param_limite) > 0):
            param_limite = "10"

        srv_paginator = Paginator(servico, param_limite)
        try:
            pagina = srv_paginator.page(param_pagina)
        except:
            pagina = srv_paginator.page(1)

        return render(
            request,
            "servicos.html",
            {
                "servicos": pagina,
                "usuario_logado": request.session.get("usuario"),
                "opcoes_qnt_por_pagina": ["10", "30", "50", "100"],
                "qnt_por_pagina": param_limite,
            },
        )
    else:
        return redirect("/login/?status=2")


def cria_servico(request):
    if request.session.get("usuario"):
        categorias = Categorias.objects.filter(servico=True)
        und_medidas = UnidadeMedida.objects.all()
        return render(
            request,
            "cria_servico.html",
            {
                "categorias": categorias,
                "und_medidas": und_medidas,
                "usuario_logado": request.session.get("usuario"),
            },
        )
    else:
        return redirect("/login/?status=2")


def valida_servico(request):
    descricao = request.POST.get("descricao")
    valor = request.POST.get("valor")
    observacao = request.POST.get("observacao")
    categoria = request.POST.get("categoria")
    und_medida = request.POST.get("und_medida")

    # cat = Categorias.objects.get(descricao = categoria)

    servico = Servicos(
        descricao=descricao,
        valor=valor,
        observacao=observacao,
        categoria_id=categoria,
        und_id=und_medida,
    )

    servico.save()
    messages.add_message(request, messages.SUCCESS, "Cadastro Realizado!")
    return redirect("/servicos")


def edita_produto(request, id):
    if request.session.get("usuario"):
        produto = Produtos.objects.get(id=id)
        categorias = Categorias.objects.filter(produto=True)
        und_medidas = UnidadeMedida.objects.all()
        if request.method == "POST":
            descricao = request.POST.get("descricao")
            preco_venda = request.POST.get("preco_venda")
            quantidade = request.POST.get("quantidade")
            categoria = request.POST.get("categoria")
            observacao = request.POST.get("observacao")
            und_medida = request.POST.get("und_medida")
            try:
                produto.descricao = descricao
                produto.preco_venda = preco_venda
                produto.quantidade = quantidade
                produto.categoria_id = categoria
                produto.observacao = observacao
                produto.und_id = und_medida
                produto.save()
                messages.add_message(request, messages.SUCCESS, "Edição realizada!")
            except:
                messages.add_message(request, messages.ERROR, "Erro ao editar Produto")
                return redirect(f"/edita_produto/{id}")
            return redirect("/produtos")
        contexto = {
            "produto": produto,
            "categorias": categorias,
            "usuario_logado": request.session.get("usuario"),
            "und_medidas": und_medidas,
        }
        return render(request, "edita_produto.html", contexto)


def edita_servico(request, id):
    if request.session.get("usuario"):
        servico = Servicos.objects.get(id=id)
        categorias = Categorias.objects.filter(servico=True)
        und_medidas = UnidadeMedida.objects.all()
        if request.method == "POST":
            descricao = request.POST.get("descricao")
            valor = request.POST.get("valor")
            categoria = request.POST.get("categoria")
            observacao = request.POST.get("observacao")
            und_medida = request.POST.get("und_medida")
            try:
                servico.descricao = descricao
                servico.valor = valor
                servico.categoria_id = categoria
                servico.observacao = observacao
                servico.und_id = und_medida
                servico.save()
                messages.add_message(request, messages.SUCCESS, "Edição realizada!")
            except:
                messages.add_message(request, messages.ERROR, "Erro ao editar Serviço")
                return redirect(f"/edita_servico/{id}")
            return redirect("/servicos")
        return render(
            request,
            "edita_servico.html",
            {
                "servico": servico,
                "categorias": categorias,
                "usuario_logado": request.session.get("usuario"),
                "und_medidas": und_medidas,
            },
        )


def excluir_produto(request, id):
    try:
        Produtos.objects.get(id=id).delete()
        messages.add_message(request, messages.SUCCESS, "Exclusão realizada!")
        return redirect("/produtos")
    except:
        messages.add_message(
            request, messages.ERROR, "Exclusão não permitida, Produto em uso no sistema"
        )
        return redirect(f"/edita_produto/{id}")


def excluir_servico(request, id):
    try:
        Servicos.objects.get(id=id).delete()
        messages.add_message(request, messages.SUCCESS, "Exclusão realizada!")
        return redirect("/servicos")
    except:
        messages.add_message(
            request, messages.ERROR, "Exclusão não permitida, Serviço em uso no sistema"
        )
        return redirect(f"/edita_servico/{id}")


def busca_cat(request):
    if request.session.get("usuario"):
        categoria = Categorias.objects.order_by("-id")
        return render(
            request,
            "/bsuca_cat.html",
            {"categoria": categoria, "usuario_logado": request.session.get("usuario")},
        )
    else:
        return redirect("/login/?status=2")


def clientes(request):
    if request.session.get("usuario"):
        termo = request.GET.get("termo")

        if termo:
            clientes = Clientes.objects.order_by("-id").filter(
                Q(razao_social__icontains=termo)
                | Q(cnpj__icontains=termo)
                | Q(cpf__icontains=termo)
                | Q(nome_completo__icontains=termo)
            )
        else:
            clientes = Clientes.objects.order_by("-id")

        param_pagina = request.GET.get("pagina", "1")
        param_limite = request.GET.get("limite", "10")

        if not (param_limite.isdigit() and int(param_limite) > 0):
            param_limite = "10"

        cli_paginator = Paginator(clientes, param_limite)
        try:
            pagina = cli_paginator.page(param_pagina)
        except:
            pagina = cli_paginator.page(1)

        contexto = {
            "clientes": pagina,
            "usuario_logado": request.session.get("usuario"),
            "opcoes_qnt_por_pagina": ["10", "30", "50", "100"],
            "qnt_por_pagina": param_limite,
        }

        return render(request, "clientes.html", context=contexto)

    return redirect("/login/?status=2")


def cria_cliente(request):
    if request.session.get("usuario"):
        form = ClienteForm()

        if request.method == "POST":
            form = ClienteForm(request.POST)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Cadastro Realizado!")
                return redirect("/clientes/")

        contexto = {"usuario_logado": request.session.get("usuario"), "form": form}
        return render(request, "cria_cliente.html", context=contexto)

    return redirect("/login/?status=2")


def excluir_cliente(request, id):
    try:
        Clientes.objects.get(id=id).delete()
        messages.add_message(request, messages.SUCCESS, "Exclusão realizada!")
        return redirect("/clientes")

    except:
        messages.add_message(
            request, messages.ERROR, "Exclusão não permitida, Cliente em uso no sistema"
        )
        return redirect(f"/edita_cliente/{id}")


def edita_cliente(request, id):
    if request.session.get("usuario"):
        cliente = Clientes.objects.get(id=id)
        form = ClienteEdtForm(instance=cliente)

        if request.method == "POST":
            form = ClienteEdtForm(request.POST, instance=cliente)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Edição realizada!")
                return redirect("/clientes/")

        contexto = {
            "usuario_logado": request.session.get("usuario"),
            "form": form,
            "cliente": cliente,
        }
        return render(request, "edita_cliente.html", context=contexto)

    return redirect("/login/?status=2")


def terceiros(request):
    if request.session.get("usuario"):
        termo = request.GET.get("termo")

        if termo:
            terceiros = Terceiros.objects.order_by("-id").filter(
                Q(razao_social__icontains=termo)
                | Q(cnpj__icontains=termo)
                | Q(cpf__icontains=termo)
                | Q(nome_completo__icontains=termo)
            )
        else:
            terceiros = Terceiros.objects.order_by("-id")

        param_pagina = request.GET.get("pagina", "1")
        param_limite = request.GET.get("limite", "10")

        if not (param_limite.isdigit() and int(param_limite) > 0):
            param_limite = "10"

        ter_paginator = Paginator(terceiros, param_limite)
        try:
            pagina = ter_paginator.page(param_pagina)
        except:
            pagina = ter_paginator.page(1)
        return render(
            request,
            "terceiros.html",
            {
                "terceiros": pagina,
                "usuario_logado": request.session.get("usuario"),
                "opcoes_qnt_por_pagina": ["10", "30", "50", "100"],
                "qnt_por_pagina": param_limite,
            },
        )

    return redirect("/login/?status=2")


def cria_terceiro(request):
    if request.session.get("usuario"):
        form = TerceiroForm()

        if request.method == "POST":
            form = TerceiroForm(request.POST)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Cadastro Realizado!")
                return redirect("/terceiros/")

        contexto = {"usuario_logado": request.session.get("usuario"), "form": form}
        return render(request, "cria_terceiro.html", context=contexto)

    return redirect("/login/?status=2")


def edita_terceiro(request, id):
    if request.session.get("usuario"):
        terceiro = Terceiros.objects.get(id=id)
        form = TerceiroEdtForm(instance=terceiro)

        if request.method == "POST":
            form = TerceiroEdtForm(request.POST, instance=terceiro)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Edição realizada!")
                return redirect("/terceiros/")

        contexto = {
            "usuario_logado": request.session.get("usuario"),
            "form": form,
            "terceiro": terceiro,
        }
        return render(request, "edita_terceiro.html", context=contexto)

    return redirect("/login/?status=2")


def excluir_terceiro(request, id):
    try:
        Terceiros.objects.get(id=id).delete()
        messages.add_message(request, messages.SUCCESS, "Exclusão realizada!")
        return redirect("/terceiros/")
    except:
        messages.add_message(
            request,
            messages.ERROR,
            "Exclusão não permitida, Terceiro em uso no sistema",
        )
        return redirect(f"/edita_terceiro/{id}")


def unidade_medida(request):
    if request.session.get("usuario"):
        termo = request.GET.get("termo")

        if termo:
            und_medidas = UnidadeMedida.objects.order_by("-id").filter(
                descricao__icontains=termo
            )
        else:
            und_medidas = UnidadeMedida.objects.order_by("-id")

        return render(
            request,
            "und_medidas.html",
            {
                "und_medidas": und_medidas,
                "usuario_logado": request.session.get("usuario"),
            },
        )

    return redirect("/login/?status=2")


def cria_und_medida(request):
    if request.session.get("usuario"):
        form = UndMedidaForm()

        if request.method == "POST":
            form = UndMedidaForm(request.POST)

            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Cadastro Realizado!")
                return redirect("/unidade_medida/")

        contexto = {"usuario_logado": request.session.get("usuario"), "form": form}
        return render(request, "cria_und_medida.html", context=contexto)

    return redirect("/login/?status=2")


def edita_und_medida(request, id):
    if request.session.get("usuario"):
        und = UnidadeMedida.objects.get(id=id)
        form = UndMedidaForm(instance=und)

        if request.method == "POST":
            form = UndMedidaForm(request.POST, instance=und)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Edição realizada!")
                return redirect("/unidade_medida/")

        contexto = {
            "usuario_logado": request.session.get("usuario"),
            "form": form,
            "und": und,
        }
        return render(request, "edita_und_medidas.html", context=contexto)

    return redirect("/login/?status=2")


def excluir_und_medida(request, id):
    try:
        UnidadeMedida.objects.get(id=id).delete()
        messages.add_message(request, messages.SUCCESS, "Exclusão realizada!")
        return redirect("/unidade_medida")
    except:
        messages.add_message(
            request,
            messages.ERROR,
            "Exclusão não permitida, Unidade de Medida em uso no sistema",
        )
        return redirect(f"/edita_und_medida/{id}")


def orcamentos(request):
    if request.session.get("usuario"):
        orcamento = Orcamentos.objects.all()

        return render(
            request,
            "orcamentos.html",
            {"usuario_logado": request.session.get("usuario"), "orcamentos": orcamento},
        )

    return redirect("/login/?status=2")


def cria_orcamento(request):
    usuario_logado = request.session.get("usuario")

    if usuario_logado:
        busca_cliente = request.GET.get("busca_cliente")
        busca_terceiro = request.GET.get("busca_terceiro")
        form = OrcamentoForm()
        form_item_factory = inlineformset_factory(
            Orcamentos, ItemOrcamento, form=ItemOrcaForm, extra=1, can_delete=True
        )
        form_item_serv_factory = inlineformset_factory(
            Orcamentos,
            ItemOrcamentoServico,
            form=ItemOrcaServForm,
            extra=1,
            can_delete=True,
        )
        form_item = form_item_factory()
        form_item_servico = form_item_serv_factory()

        resultado_cliente = {}
        resultado_terceiro = {}

        if busca_cliente:
            cliente = Clientes.objects.filter(
                Q(razao_social__icontains=busca_cliente)
                | Q(cnpj__icontains=busca_cliente)
                | Q(cpf__icontains=busca_cliente)
                | Q(nome_completo__icontains=busca_cliente)
            ).first()
            #form["cliente"].value = cliente
            if cliente:
                form.fields['cliente'].initial = cliente.id

                if cliente.nome_completo:
                    resultado_cliente['cliente_encontrado'] = cliente.nome_completo
                    resultado_cliente['cliente_id'] = cliente.id

                else:
                    resultado_cliente['cliente_encontrado'] = cliente.razao_social

            else:
                resultado_cliente['cliente_encontrado'] = None
            
            return JsonResponse(resultado_cliente)

        if busca_terceiro:
            terceiro = Terceiros.objects.filter(
                Q(razao_social__icontains=busca_terceiro)
                | Q(cnpj__icontains=busca_terceiro)
                | Q(cpf__icontains=busca_terceiro)
                | Q(nome_completo__icontains=busca_terceiro)
            ).first()
            #form["terceiro"].value = terceiro
            if terceiro:
                form.fields['terceiro'].initial = terceiro.id

                if terceiro.nome_completo:
                    resultado_terceiro['terceiro_encontrado'] = terceiro.nome_completo

                else:    
                    resultado_terceiro['terceiro_encontrado'] = terceiro.razao_social

            else:
                resultado_terceiro['terceiro_encontrado'] = None
  
            return JsonResponse(resultado_terceiro)

        usuario = Usuario.objects.filter(id=usuario_logado).first()
        form["usuario"].value = usuario

        if request.method == "POST":
            form = OrcamentoForm(request.POST)
            form_item_factory = inlineformset_factory(
                Orcamentos, ItemOrcamento, form=ItemOrcaForm
            )
            form_item_serv_factory = inlineformset_factory(
                Orcamentos, ItemOrcamentoServico, form=ItemOrcaServForm
            )
            form_item = form_item_factory(request.POST)
            form_item_servico = form_item_serv_factory(request.POST)

            total_form = request.POST.get("itens-TOTAL_FORMS")
            i = 0
            valor_total_item = 0
            valor_total_servico = 0

            while i < int(total_form):
                print("entrou no While")
                if form_item[i]["item_valor"].value():
                    print("Entrou no IF Produto")
                    valor_total_item += float(form_item[i]["item_valor"].value()) * float(
                        form_item[i]["quantidade"].value()
                    )
                if form_item_servico[i]["item_valor_servico"].value():
                    print("Entrou no IF Serviço")
                    valor_total_servico += float(
                        form_item_servico[i]["item_valor_servico"].value()
                    ) * float(form_item_servico[i]["quantidade"].value())
                i += 1

            if (
                form.is_valid()
                and form_item.is_valid()
                and form_item_servico.is_valid()
            ):
                orcamento = form.save(commit=False)
                orcamento.valor = valor_total_item + valor_total_servico
                orcamento.save()
                form_item.instance = orcamento
                form_item_servico.instance = orcamento
                form_item.save()
                form_item_servico.save()
                messages.add_message(request, messages.SUCCESS, "Cadastro Realizado!")
                return redirect("/orcamentos/")

            else:
                print(form.errors)
                print(form_item.errors)

        contexto = {
            "usuario_logado": usuario_logado,
            "form": form,
            "form_item": form_item,
            "form_item_servico": form_item_servico,
        }
        return render(request, "cria_orcamento.html", context=contexto)

    return redirect("/login/?status=2")


def edita_orcamento(request, id):
    usuario_logado = request.session.get("usuario")

    if usuario_logado:
        orcamento = Orcamentos.objects.get(id=id)

        if request.method == "GET":
            form = OrcamentoForm(instance=orcamento)
            form["usuario"].value = orcamento.usuario
            form["cliente"].value = orcamento.cliente
            form["terceiro"].value = orcamento.terceiro
            form_item_factory = inlineformset_factory(
                Orcamentos, ItemOrcamento, form=ItemOrcaForm, extra=1, can_delete=True
            )
            form_item_serv_factory = inlineformset_factory(
                Orcamentos,
                ItemOrcamentoServico,
                form=ItemOrcaServForm,
                extra=1,
                can_delete=True,
            )
            form_item = form_item_factory(instance=orcamento)
            form_item_servico = form_item_serv_factory(instance=orcamento)

            context = {
                "usuario_logado": usuario_logado,
                "form": form,
                "form_item": form_item,
                "form_item_servico": form_item_servico,
                "orcamento": orcamento,
            }

            return render(request, "edita_orcamento.html", context)

        elif request.method == "POST":
            form = OrcamentoForm(request.POST, instance=orcamento)
            form_item_factory = inlineformset_factory(
                Orcamentos, ItemOrcamento, form=ItemOrcaForm
            )
            form_item_serv_factory = inlineformset_factory(
                Orcamentos, ItemOrcamentoServico, form=ItemOrcaServForm
            )
            form_item = form_item_factory(request.POST, instance=orcamento)
            form_item_servico = form_item_serv_factory(request.POST, instance=orcamento)

            if (
                form.is_valid()
                and form_item.is_valid()
                and form_item_servico.is_valid()
            ):
                form.save()
                form_item.save()
                form_item_servico.save()
                messages.add_message(request, messages.SUCCESS, "Edição realizada!")
                return redirect(reverse("orcamentos"))

            context = {
                "usuario_logado": usuario_logado,
                "form": form,
                "form_item": form_item,
                "form_item_servico": form_item_servico,
            }

            return render(request, "edita_orcamento.html", context)

    return redirect("/login/?status=2")


def excluir_orcamento(request, id):
    try:
        Orcamentos.objects.get(id=id).delete()
        messages.add_message(request, messages.SUCCESS, "Exclusão realizada!")
        return redirect("/orcamentos")
    except:
        messages.add_message(
            request,
            messages.ERROR,
            "Exclusão não permitida, Orçamento em uso no sistema",
        )
        return redirect(f"/edita_orcamento/{id}")
