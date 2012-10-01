from django.http import HttpResponse
from django.shortcuts import render, render_to_response

def home(request):
    return render(request, 'index.html')


def freshmen(request):
    return HttpResponse('frosh')

def sophomore(request):
    return HttpResponse('soph')

def junior(request):
    return HttpResponse('jr')

def senior(request):
    return HttpResponse('sr')


