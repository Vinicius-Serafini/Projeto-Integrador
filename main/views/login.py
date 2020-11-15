from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from main.models import Usuario

def login(request):
    if request.method == "POST":
        usuario = Usuario.objects.filter(email = request.POST['email'], senha = request.POST['senha'])
        if usuario.count() > 0:
            request.session['login_id'] = usuario[0].id

            return redirect('/')
        # terminar

    return render(request, 'main/login/index.html') 