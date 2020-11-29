from django.shortcuts import render, redirect
from django.http import HttpResponse

def logout(request):
    if 'login_id' in request.session:
        del request.session['login_id']

    return redirect('/login')
