from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from main.models import Publicacao
from main.models import Usuario

def minhas_publicacoes(request):
    
    if 'login_id' not in request.session:
        return redirect('/login')


    publicacoes = Publicacao.objects.all().filter(usuario = get_object_or_404(Usuario, pk=request.session['login_id']))
    
    context = {
        'publicacoes' : publicacoes,
        'usu_id' : request.session['login_id'],
    }
    
    return render(request, 'main/homepage/index.html', context)