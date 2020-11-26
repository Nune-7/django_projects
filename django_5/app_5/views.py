from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import NewTask
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = "login")
def home(request):
    tasks = NewTask.objects.all().filter(user=request.user)

    content = {'tasks': tasks}
    return render(request, "app_5/home.html", content)

@login_required(login_url = "login")
def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task= form.save(commit=False)
            task.user=User.objects.get(id=request.user.id)
            task.save()

        return redirect('home')

    form = TaskForm()
    content = {'form': form}

    return render(request, "app_5/new_task.html", content)


def task_view(request, pk):
    task = NewTask.objects.get(id=pk)
    content = {'task': task}
    return render(request, "app_5/task_view.html", content)


def task_update(request, pk):
    task = NewTask.objects.get(id=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

        return redirect('home')

    form = TaskForm(instance=task)
    content = {'form': form}
    return render(request, "app_5/task_update.html", content)


def task_delete(request, pk):
    task = NewTask.objects.get(id=pk)
    task.delete()
    messages.add_message(request, messages.SUCCESS, "User deleted the task.")
    return redirect("home")