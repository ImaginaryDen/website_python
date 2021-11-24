from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'task': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def sort_func(request, sort=1):
    if sort != 1:
        sort = -1
    tasks = Task.objects.order_by('time')[::sort]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'task': tasks})


def post(request, item_id):
    items = Task.objects.all()
    item = [x for x in items if x.id == item_id]
    return render(request, 'main/post.html', {'title': 'Пост', 'item': item[0]})
