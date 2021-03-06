from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from main.models import Publicacao
from main.models import Usuario
from main.models import Favorito


def salvar_publicacao_favoritos(request, id):

    if 'login_id' in request.session:
    
        publicacao = get_object_or_404(Publicacao, pk=id)
        usuario = get_object_or_404(Usuario, pk=request.session['login_id'])

        favorito = Favorito(usuario = usuario,
                            publicacao = publicacao)
        
        favorito.save()

        
        return redirect('/')

    return redirect('/')
