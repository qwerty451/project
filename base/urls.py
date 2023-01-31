from django.contrib import admin
from django.urls import path
from django.urls.conf import include


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', include('user.urls')),
    path('tasks/', include('task.urls')),
]