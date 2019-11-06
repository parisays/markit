from django.db import models
from users.models import User

class Calendar(models.Model):
    """
    Calendar model.
    """
    Twitter = 'Twitter'
    Facebook = 'Facebook'
    PLATFORM_CHOICES = [
        (Twitter, 'Twitter'),
        (Facebook, 'Facebook'),
    ]
    name = models.CharField(max_length=100)
    collaborators = models.ManyToManyField(User, related_name='collaborators', default=[])
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    connected_platforms = models.CharField(max_length=8,
                                           choices=PLATFORM_CHOICES,
                                           default=None,
                                           null=True,
                                           blank=True)

    def __str__(self):
        return self.name
