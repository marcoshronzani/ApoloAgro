from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


def login(request):
    if request.session.get("usuario"):
        return redirect("/home")
    status = request.GET.get("status")
    return render(request, "login.html", {"status": status})


def cadastro(request):
    # if request.session.get('usuario'):
    # status = request.GET.get('status')
    return render(request, "cadastro.html")


def valida_cadastro(request):
    nome = request.POST.get("nome")
    senha = request.POST.get("senha")
    email = request.POST.get("email")

    usuario = Usuario.objects.filter(email=email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect("/cadastro/?status=1")

    if len(senha) < 8:
        return redirect("/cadastro/?status=2")

    if len(usuario) > 0:
        return redirect("/cadastro/?status=3")

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome, senha=senha, email=email)
        usuario.save()

        return redirect("/login/?status=0")
    except:
        return redirect("/login/?status=4")


def validar_login(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(senha=senha)

    if len(usuario) == 0:
        return redirect("/login/?status=1")
    elif len(usuario) > 0:
        request.session["usuario"] = usuario[0].id
        return redirect(f'/home/?id_usuario={request.session["usuario"]}')

    return HttpResponse(f"{email} {senha}")


def sair(request):
    request.session.flush()
    return redirect("/login/")
