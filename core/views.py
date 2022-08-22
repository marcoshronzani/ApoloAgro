from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    contexto = {'nome': 'Apolo Agro'}
    return render(request, 'home.html', context=contexto)


def cliente(request):
    contexto = {'nome': 'Cliente'}
    return render(request, 'home.html', context=contexto)
