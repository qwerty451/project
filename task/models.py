from django.db import models
from django.contrib.auth.models import User

OFFICIALTASK_CHOICES = (
    ("Fit", "Fitness"),
    ("Chore", "Chores"),
    ("Work", "Work"),
    ("Read", "Reading"),
    ("Journal", "Journaling"),
    ("Study", "Studying"),
    ("HealthEat", "Healthy Eating"),
    ("HealthSleep", "Healthy Sleeping"),
    
)

# Model to store keep track which user is part of which task in the choicefield
class OfficialTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100, choices=OFFICIALTASK_CHOICES)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.task

# Model to store custom tasks created by the user    
class CustomTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.task
