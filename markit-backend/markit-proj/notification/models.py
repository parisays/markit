from uuid import uuid4
from django.db import models
from calendars.models import Calendar
from users.models import User
from collaboration.models import Collaborator


class Notification(models.Model):
    created = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Invitation(Notification):
    token = models.CharField(max_length=255, null=True)
    calendar = models.ForeignKey(Calendar,
                                 on_delete=models.CASCADE, related_name='calendar_invitations')
    invited = models.ForeignKey(Collaborator,
                                on_delete=models.CASCADE, related_name='user_invitations')
    inviter = models.ForeignKey(Collaborator,
                                on_delete=models.CASCADE, related_name='collaborator_invitations')
    
    def save(self, *args, **kwargs):
        while True:
            try:
                if not self.token:
                    self.token = uuid4().hex
                return super(Invitation, self).save(*args, **kwargs)
            except:
                continue



