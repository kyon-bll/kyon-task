from django.shortcuts import render
from django.utils import timezone

from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    now = timezone.now()
    return render(request, 'task/task_list.html', {'tasks': tasks, 'now': now})
