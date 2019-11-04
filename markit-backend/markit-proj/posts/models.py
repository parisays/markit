from django.db import models
from calendars.models import Calendar

class Post(models.Model):
    """
    Post model.
    """
    name = models.CharField(max_length=100)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()

    def __str__(self):
        return self.name + ' | ' + self.calendar.name
