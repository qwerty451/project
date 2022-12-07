from django.contrib import admin

# Register your models here.

from .models import Player, Task, Buddy

admin.site.register(Player)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'country', 'created_at', 'updated_at')

admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('player', 'task', 'description', 'created_at', 'updated_at')

admin.site.register(Buddy)
class BuddyAdmin(admin.ModelAdmin):
    list_display = ('main_player', 'buddy_player')

