from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'menu/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'menu/about.html')

def create(request):
    return render(request, 'menu/create.html')

