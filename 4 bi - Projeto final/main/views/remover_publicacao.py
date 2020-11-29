from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from main.models.publicacao import Publicacao

def remover_publicacao(request, id):

    if 'login_id' in request.session:
    
        publicacao = get_object_or_404(Publicacao, pk=id)

        if publicacao.usuario.id == request.session['login_id']:
            publicacao.delete()
        return redirect('/')

    return redirect('/')
