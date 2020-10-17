from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

card = [
    {"id" : 1},
    {"id" : 2},
    {"id" : 3},
    {"id" : 4},
]


def homepage(request):
    context = {
        'cards' : card
        }
    return render(request, 'main/homepage/index.html', context)

def login(request):
    return render(request, 'main/login/index.html') 

def cadastro(request):
    return render(request, 'main/cadastro/index.html')

def nova_publicacao(request):
    return render(request, 'main/nova_publicacao/index.html') 

def publicacao_detalhes(request):
    return render(request, 'main/publicacao_detalhes/index.html')