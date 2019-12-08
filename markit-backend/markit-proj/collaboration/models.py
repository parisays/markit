from django.db import models
from jsonfield import JSONField
from users.models import User


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
    access = JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="", blank=True, null=True)

    def __str__(self):
        return self.user.email + '|' + self.role
