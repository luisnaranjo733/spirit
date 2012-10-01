from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def home(request):
    return render(request, 'index.html')


def freshmen(request):
    return HttpResponse('frosh')


def sophomores(request):
    return HttpResponse('soph')


def juniors(request):
    return HttpResponse('jr')


def seniors(request):
    return HttpResponse('sr')

