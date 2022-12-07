from django.contrib import admin

# Register your models here.

from .models import Users, Tasks, Buddy

admin.site.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'country', 'created_at', 'updated_at')

admin.site.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'description', 'created_at', 'updated_at')

admin.site.register(Buddy)
class BuddyAdmin(admin.ModelAdmin):
    list_display = ('user', 'user2')

