from django.db import models
from users.models import User

class Calendar(models.Model):
    """
    Calendar model.
    """
    name = models.CharField(max_length=100)
    collaborators = models.ManyToManyField(User, related_name='collaborators', default=[])
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
