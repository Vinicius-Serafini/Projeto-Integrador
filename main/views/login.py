from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    if request.name == "POST":
        pass

    return render(request, 'main/login/index.html') 