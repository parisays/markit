from rest_framework import serializers
from calendars.serializers import CalendarSerializer
from .models import Collaborator

class CollaboratorSerializer(serializers.ModelSerializer):
    """
    Collaborator serializer.
    """
    # access = serializers.JSONField()
    class Meta:
        model = Collaborator
        fields = ('user', 'calendar', 'role')
