from django.shortcuts import render, HttpResponse, redirect

from project_app.models import Users

import random

# Create a view that shows a list of all users
def index(request):
    # Get all users from database
    users = Users.objects.all()
    # Pass users to template
    context = {
        'users': users
    }
    # Render template
    return render(request, 'index.html', context)

# Create a view that shows a single user
def show(request):
    # Use random to get a random user
    user = Users.objects.order_by('?').first()
    # Pass user to template
    context = {
        'user': user
    }
    # Show context directly without rendering a template
    return HttpResponse(f"User: {user.name}")