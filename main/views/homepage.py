from django.shortcuts import render
from django.http import HttpResponse

card = [
    {"id" : 1},
    {"id" : 2},
    {"id" : 3},
    {"id" : 4},
]


def homepage(request):
    context = {
        'cards' : card
        }
    return render(request, 'main/homepage/index.html', context)