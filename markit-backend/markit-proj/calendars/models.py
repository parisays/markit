from django.db import models
from allauth.socialaccount.models import SocialAccount
from users.models import User
from collaboration.models import Collaborator

class Calendar(models.Model):
    """
    Calendar model.
    """
    Twitter = 'Twitter'
    Facebook = 'Facebook'
    FT = 'Facebook and Twitter'
    PLATFORM_CHOICES = [
        (Twitter, 'Twitter'),
        (Facebook, 'Facebook'),
        (FT, 'Facebook and Twitter'),
    ]

    name = models.CharField(max_length=100)
    collaborators = models.ManyToManyField(Collaborator, related_name='calendar_collaborators',
                                           default=[], blank=True)

    # managers = models.ManyToManyField(User, related_name='calendar_managers',
    #                                   default=[], blank=True)

    # editors = models.ManyToManyField(User, related_name='calendar_editors',
    #                                  default=[], blank=True)

    # viewers = models.ManyToManyField(User, related_name='calendar_viewers',
                                    #  default=[], blank=True)

    owner = models.ForeignKey(User, related_name='calendar_owner', on_delete=models.CASCADE)

    connectedPlatforms = models.CharField(max_length=20,
                                          choices=PLATFORM_CHOICES,
                                          default="",
                                          null=True,
                                          blank=True)


    def __str__(self):
        return self.name
