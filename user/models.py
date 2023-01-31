from django.db import models

from django.contrib.auth.models import User

# Model to store the profile info of each user and extend the User model.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #TODO change from webserver storage to AWS storage solution.
    bio = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=100, blank=True)
    connections = models.ManyToManyField(User, related_name='connections', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# Model to store the accuracy of each user.
class UserAccuracy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accuracy = models.IntegerField(default=100)

    def __str__(self):
        return f'{self.user.username} Accuracy'

# Model to keep track of stats for each user.
class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Stats'

# Model to store the streak for each user.
class UserStreak(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Streak'

# Model to store the settings for each user.
class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=8, default='en')
    theme = models.CharField(max_length=8, default='light')
    #timezone = models.CharField(max_length=100, default='UTC')

    def __str__(self):
        return f'{self.user.username} Settings'

# Model to store the Buddy for each user. The buddy is another user.
class Buddy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='main_user')
    buddy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_buddy', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Buddy'