from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    player = models.ForeignKey(Player, related_name="task", on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

class Buddy(models.Model):
    main_player = models.ForeignKey(Player, related_name="main_player", on_delete=models.CASCADE, null=True, blank=True)
    buddy_player = models.ForeignKey(Player, related_name="buddy_player", on_delete=models.CASCADE, null=True, blank=True)