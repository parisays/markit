from rest_framework import serializers
from .models import Collaborator

class CollaboratorSerializer(serializers.ModelSerializer):
    """
    Collaborator serializer.
    """
    access = serializers.JSONField()
    class Meta:
        model = Collaborator
        fields = ('access', 'user', 'role')
