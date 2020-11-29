from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from main.models import Publicacao
from main.models import Usuario
from main.models import Favorito

def publicacoes_salvas(request):
    
    if 'login_id' not in request.session:
        return redirect('/login')

    publicacoes_salvas = []

    for favorito in Favorito.objects.filter(usuario=get_object_or_404(Usuario, pk=request.session['login_id'])):
        publicacoes_salvas.append(favorito.publicacao)


    context = {
        'publicacoes' : publicacoes_salvas,
        'usu_id' : request.session['login_id'],
        'publicacoes_salvas': publicacoes_salvas,
    }
    
    return render(request, 'main/homepage/index.html', context)