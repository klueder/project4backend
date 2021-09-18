from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    user_icon_url = models.TextField()
    user_points = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    task_title = models.CharField(max_length=100)
    task_point_value = models.IntegerField()
    task_icon_url = models.TextField()
    complete = models.BooleanField()

    def __str__(self):
        return self.task_title

class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rewards')
    reward_title = models.CharField(max_length=100)
    reward_point_value = models.IntegerField()
    reward_icon_url = models.TextField()
    reward_earned = models.BooleanField()

    def __str__(self):
        return self.reward_title