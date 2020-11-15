from django.shortcuts import render
from django.http import HttpResponse

from main.models import Usuario

def cadastrar(request):
    if request.method == "POST":

        usuario = Usuario(email = request.POST['email'],
                    senha =  request.POST['senha'],
                    nome = request.POST['nome'],
                    cidade = request.POST['cidade'],
                    uf = request.POST['uf'],
                    )

        usuario.save()     
    
    
    return render(request, 'main/cadastro/index.html')