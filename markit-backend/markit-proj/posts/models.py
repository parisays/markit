import os
from django.db import models
from calendars.models import Calendar
from markit.settings import MEDIA_URL, MEDIA_ROOT

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
    image = models.ImageField(upload_to='posts/', default='posts/postDefault.png')

    def __str__(self):
        return self.subject + ' | ' + self.calendar.name