from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.models import Publicacao
from main.models import Usuario

def nova_publicacao(request):
    if 'login_id' not in request.session:
        return redirect('/login')

    if request.method == "POST":

        publicacao = Publicacao(
            usuario = Usuario.objects.filter(id = request.session['login_id'])[0],
            titulo = request.POST['titulo'],
            descricao = request.POST['descricao'],
            email = request.POST['email'],
            whatsapp = request.POST['whatsapp'],
            roupa = True if 'roupas' in request.POST else False,
            alimento = True if 'alimentos' in request.POST else False,
            dinheiro = True if 'dinheiro' in request.POST else False
        )

        publicacao.save()

        return redirect('/')


    return render(request, 'main/nova_publicacao/index.html') 