from django.db import models
from allauth.socialaccount.models import SocialAccount
from users.models import User

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
    collaborators = models.ManyToManyField(User, related_name='calendar_collaborators',
                                           default=[], blank=True)
    owner = models.ForeignKey(User, related_name='calendar_owner', on_delete=models.CASCADE)
    connectedPlatforms = models.CharField(max_length=20,
                                          choices=PLATFORM_CHOICES,
                                          default="",
                                          null=True,
                                          blank=True)

    class Meta:
        permissions = (
            ('can_view', 'Viewer'),
            # ('can_edit', 'Editor'),
            # ('can_manage', 'Manager'),
        )

    def __str__(self):
        return self.name
