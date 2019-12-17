from django.db import models
from calendars.models import Calendar
from users.models import User
from collaboration.models import Collaborator

class Invitation(models.Model):
    calendar = models.ForeignKey(Calendar,
                                 on_delete=models.CASCADE, related_name='calendar_invitations')
    invited = models.ForeignKey(Collaborator,
                                on_delete=models.CASCADE, related_name='user_invitations')
    inviter = models.ForeignKey(Collaborator,
                                on_delete=models.CASCADE, related_name='collaborator_invitations')

  