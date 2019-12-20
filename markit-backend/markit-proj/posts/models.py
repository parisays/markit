from django.db import models
from django_celery_beat.models import PeriodicTask
from calendars.models import Calendar

class Post(models.Model):
    """
    Post model.
    """

    Draft = 'Draft'
    Published = 'Published'
    Scheduled = 'Scheduled'
    STATUS_CHOICES = [
        (Draft, 'Draft'),
        (Published, 'Published'),
        (Scheduled, 'Scheduled'),
    ]

    subject = models.CharField(max_length=100)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=Draft)
    image = models.ImageField(upload_to='posts/', default='posts/postDefault.png')
    publishDateTime = models.DateTimeField(verbose_name='Publish Date and Time',
                                           blank=True, null=True, default=None)
    publishTask = models.ForeignKey(PeriodicTask, on_delete=models.SET_DEFAULT,
                                    related_name='post_publish_task', null=True, default=None)

    def __str__(self):
        return self.subject + ' | ' + self.calendar.name
