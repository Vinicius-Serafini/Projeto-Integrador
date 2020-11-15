from django.shortcuts import render, redirect
from django.http import HttpResponse

def logout(request):
    del request.session['login_id']

    return redirect('/login')
