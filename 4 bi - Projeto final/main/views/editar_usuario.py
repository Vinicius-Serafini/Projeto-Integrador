from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from main.models import Usuario

def editar_usuario(request, id):

    if 'login_id' in request.session:

        usuario = get_object_or_404(Usuario, pk=id)

        if request.session['login_id'] == usuario.id:

            context = {
                'usuario' : usuario,    
                'usu_id' : request.session['login_id'],
            }

            if request.method == "POST":

                usuario.email = request.POST['email']
                usuario.senha =  request.POST['senha']
                usuario.nome = request.POST['nome']
                usuario.cidade = request.POST['cidade']
                usuario.uf = request.POST['uf'] if 'dinheiro' in request.POST else usuario.uf

                print(usuario)

                usuario.save()  
    
            return render(request, 'main/editar_usuario/index.html', context)
 
        return redirect('/')

    return redirect('/login')