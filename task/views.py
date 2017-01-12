from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    now = timezone.now()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            form = TaskForm()
    else:
        form = TaskForm()
    return render(request, 'task/task_list.html', {'tasks': tasks, 'now': now, 'form': form})
