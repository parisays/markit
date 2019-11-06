from django.db import models
from calendars.models import Calendar

class Post(models.Model):
    """
    Post model.
    """
    Draft = 'Draft'
    Published = 'Published'
    STATUS_CHOICES = [
        (Draft, 'Draft'),
        (Published, 'Published'),
    ]
    subject = models.CharField(max_length=100)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=Draft)

    def __str__(self):
        return self.subject + ' | ' + self.calendar.name
