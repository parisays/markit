from django.db import models
from allauth.socialaccount.models import SocialAccount
from users.models import User

class Calendar(models.Model):
    """
    Calendar model.
    """
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='calendar_users')
    socials = models.ManyToManyField(SocialAccount, related_name='calendar_socials')

    def __str__(self):
        return self.name
