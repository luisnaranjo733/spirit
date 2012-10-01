from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from generation.models import Generation, Student

today = datetime.now()

if 9 <= today.month < 12: # if between september and december, compensate
    current_grad = today.year + 1
elif today.month >= 1:
    current_grad = today.year
# current_grad is current senior grad year

current = {
        'freshmen': current_grad + 3,
        'sophomores': current_grad + 2,
        'juniors': current_grad + 1,
        'seniors': current_grad
}


def getGen(genName):
    generation = Generation.objects.get(graduation=current[genName])
    generation.name = genName
    return generation

def home(request):
    return render(request, 'index.html')


def freshmen(request):
    params = {'gen': getGen('freshmen')}
    return render(request, 'generation/freshmen.html', params)


def sophomores(request):
    params = {'gen': getGen('sophomores')}
    return render(request, 'generation/sophomores.html', params)


def juniors(request):
    params = {'gen': getGen('juniors')}
    return render(request, 'generation/juniors.html', params)


def seniors(request):
    params = {'gen': getGen('seniors')}
    return render(request, 'generation/seniors.html', params)

