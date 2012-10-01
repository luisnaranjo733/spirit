from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def home(request):
    return render(request, 'index.html')


def freshmen(request):
    return render(request, 'class/freshmen.html')


def sophomores(request):
    return render(request, 'class/sophomores.html')


def juniors(request):
    return render(request, 'class/juniors.html')


def seniors(request):
    return render(request, 'class/seniors.html')

