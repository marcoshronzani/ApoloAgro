from django.shortcuts import render


def clientes(request):
    contexto = {'nome': 'Apolo Agro'}
    return render(request, 'clientes.html', context=contexto)


def categorias(resquest):
    return render(resquest, 'categorias.html')
