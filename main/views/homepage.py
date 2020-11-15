from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.models import Publicacao

def homepage(request):
    
    if 'login_id' not in request.session:
        return redirect('/login')


    context = {
        'publicacoes' : Publicacao.objects.all()
        }
    
    return render(request, 'main/homepage/index.html', context)