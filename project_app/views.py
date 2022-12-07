from django.shortcuts import render, HttpResponse, redirect

from project_app.models import Player, Task, Buddy

def index(request):
    context = {
        "all_users": Player.objects.all()
    }
    return render(request, "project_app/index.html", context)

def task(request):
    return render(request, "project_app/task.html", context)