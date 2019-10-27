from django.db import models
from users.models import User

class Calendar(models.Model):
    """
    Calendar model.
    """
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User, related_name='calendars')

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    Post model.
    """
    name = models.CharField(max_length=100)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()

    def __str__(self):
        return self.name + ' | ' + self.calendar.name
