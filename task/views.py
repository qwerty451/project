from django.shortcuts import render
from .models import *

# Create your views here.

def taskOverview(request):
    # Get all official and unofficial tasks of the user
    official_tasks = OfficialTask.objects.filter(user=request.user)
    custom_tasks = CustomTask.objects.filter(user=request.user)
    # Check if both are empty
    if not official_tasks and not custom_tasks:
        context = {
            'empty': True
        }
    else:
        context = {
            'official_tasks': official_tasks,
            'custom_tasks': custom_tasks,
            'empty': False
        }
    return render(request, 'task/taskOverview.html', context)