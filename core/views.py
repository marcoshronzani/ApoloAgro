from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario


# Create your views here.


def home(request):
    if request.session.get("usuario"):
        contexto = {"nome": "Apolo Agro"}
        usuario = Usuario.objects.get(id=request.session["usuario"])
        return render(
            request, "home.html", {"usuario_logado": request.session.get("usuario")}
        )
    else:
        return redirect("/login/?status=2")


def cliente(request):
    contexto = {"nome": "Cliente"}
    return render(request, "home.html", context=contexto)
