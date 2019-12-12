from django.db import models
from jsonfield import JSONField
from users.models import User
from calendars.models import Calendar

class Role(models.Model):
    """
    Role model.
    """
    name = models.CharField(max_length=150)
    access = JSONField()

    def __str__(self):
        return self.name


class Collaborator(models.Model):
    """
    Collaborator model.
    """
    user = models.ForeignKey(User, related_name='collaborator_user', on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, related_name='collaborator_calendar',
                                 on_delete=models.CASCADE)
    role = models.ForeignKey(Role, related_name='collaborator_role',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email + ' is a ' + self.role.name + ' of ' + self.calendar.name
