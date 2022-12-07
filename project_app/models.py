from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tasks(models.Model):
    user = models.ForeignKey(Users, related_name="tasks", on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

class Buddy(models.Model):
    user = models.ForeignKey(Users, related_name="buddy", on_delete=models.CASCADE, null=True, blank=True)
    user2 = models.ForeignKey(Users, related_name="buddy2", on_delete=models.CASCADE, null=True, blank=True)