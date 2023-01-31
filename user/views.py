from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registerView(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)