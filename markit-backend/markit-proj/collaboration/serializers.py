from rest_framework import serializers
from calendars.serializers import CalendarSerializer
from .models import Collaborator, Role

class RoleSerializer(serializers.ModelSerializer):
    """
    Role serializer.
    """
    access = serializers.JSONField()
    class Meta:
        model = Role
        fields = ('name', 'access')


class CollaboratorSerializer(serializers.ModelSerializer):
    """
    Collaborator serializer.
    """
    # access = serializers.JSONField()
    role = RoleSerializer(many=True, read_only=True)
    class Meta:
        model = Collaborator
        fields = ('user', 'calendar', 'role')
