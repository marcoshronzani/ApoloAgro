from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def login(request):
    return HttpResponse('login')

def cadastro(request):
    return render(request, 'cadastro.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')

    return HttpResponse(f"{nome} {senha} {email}")