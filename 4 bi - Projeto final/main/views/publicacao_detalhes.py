from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from main.models import Publicacao

def publicacao_detalhes(request, id):

    if 'login_id' not in request.session:
        return redirect('/login')
    
    publicacao = get_object_or_404(Publicacao, pk=id)
    print(publicacao)

    context = {
        'publicacao' : publicacao,
        'usu_id' : request.session['login_id']
    }

    return render(request, 'main/publicacao_detalhes/index.html', context)