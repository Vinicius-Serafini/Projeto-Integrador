from django.shortcuts import render
from django.http import HttpResponse

def nova_publicacao(request):
    return render(request, 'main/nova_publicacao/index.html') 