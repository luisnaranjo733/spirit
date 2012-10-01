from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response

from generation.models import Generation, Student

today = datetime.now()

if 9 <= today.month <= 12: # if between september and december, compensate
    current_grad = today.year + 1
elif today.month >= 1:
    current_grad = today.year
# current_grad is current senior grad year
current_years = [
        current_grad + 3,
        current_grad + 2,
        current_grad + 1,
        current_grad
]

current = {
        'freshmen': current_years[0],
        'sophomores': current_years[1],
        'juniors': current_years[2],
        'seniors': current_years[3],
}


def getGen(genName):
    try:
        generation = Generation.objects.get(graduation=current[genName])
    except Generation.DoesNotExist, tb:
        print(tb)
        raise Http404
    generation.name = genName
    return generation


def getAll():
    for generation in Generation.objects.all():
        if int(generation.graduation) in current_years:
            yield generation


def home(request):
    highest = Generation.objects.order_by('points').reverse()
    highest = list(highest)
    for generation in highest:
        if generation.graduation not in current_years:
            highest.remove(generation)

    params = {'winner': highest[0]}
    return render(request, 'index.html', params)


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

