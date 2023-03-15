from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('index')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)


def updateTask(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'update_task.html', context)

def deleteTask(request, id):
    item = Task.objects.get(id=id)
    contex = {'item':item}
    if request.method == 'POST':
        item.delete()
        return redirect('index')

    return render(request, 'delete_item.html', contex)

def test(request):
    return render(request, 'test.html')