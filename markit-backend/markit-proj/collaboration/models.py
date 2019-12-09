from django.db import models
# from jsonfield import JSONField
from users.models import User
from calendars.models import Calendar

class Collaborator(models.Model):
    """
    Collaborator model.
    """
    Owner = 'Owner'
    Manager = 'Manager'
    Editor = 'Editor'
    Viewer = 'Viewer'
    ROLE_CHOICES = [
        (Owner, 'Owner'),
        (Manager, 'Manager'),
        (Editor, 'Editor'),
        (Viewer, 'Viewer'),
    ]

    user = models.ForeignKey(User, related_name='collaborator_user', on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, related_name='collaborator_calendar', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="", blank=True, null=True)
    # access = JSONField()

    def __str__(self):
        return self.user.email + '|' + self.calendar.name + '|' + self.role
