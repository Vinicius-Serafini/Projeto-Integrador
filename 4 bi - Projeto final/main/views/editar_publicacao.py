from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from main.models import Publicacao
from main.models import Usuario

def editar_publicacao(request, id):
    if 'login_id' not in request.session:
        return redirect('/login')

    publicacao = get_object_or_404(Publicacao, pk=id)

    if request.session['login_id'] != publicacao.usuario.id:
        return redirect('/')

    if request.method == "POST":

        publicacao.titulo = request.POST['titulo']
        publicacao.descricao = request.POST['descricao']
        publicacao.email = request.POST['email']
        publicacao.whatsapp = request.POST['whatsapp']
        publicacao.roupa = True if 'roupas' in request.POST else False
        publicacao.alimento = True if 'alimentos' in request.POST else False
        publicacao.dinheiro = True if 'dinheiro' in request.POST else False

        publicacao.save()

        return redirect('/')

    context = {
        'publicacao': publicacao,
        'usu_id': request.session['login_id']
    }


    return render(request, 'main/editar_publicacao/index.html', context) 