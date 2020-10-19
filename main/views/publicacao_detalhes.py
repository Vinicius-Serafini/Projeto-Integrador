from django.shortcuts import render
from django.http import HttpResponse


def publicacao_detalhes(request):
    return render(request, 'main/publicacao_detalhes/index.html')