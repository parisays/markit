from rest_framework import serializers
from .models import Collaborator, Role


class RoleSerializer(serializers.ModelSerializer):
    """
    Role serializer.
    """
    access = serializers.JSONField()
    class Meta:
        model = Role
        fields = ('id', 'name', 'access',)
        read_only_fields = ('id',)


class CollaboratorSerializer(serializers.ModelSerializer):
    """
    Collaborator serializer.
    """
    role = RoleSerializer()
    firstName = serializers.CharField(source='user.firstName')
    lastName = serializers.CharField(source='user.lastName')
    email = serializers.EmailField(source='user.email')
    class Meta:
        model = Collaborator
        fields = ('id', 'user', 'firstName', 'lastName',
                  'email', 'calendar', 'role', 'isConfirmed',)
        read_only_fields = ('id',)


class CollaboratorCreateSerializer(serializers.ModelSerializer):
    """
    Collaborator serializer.
    """
    class Meta:
        model = Collaborator
        fields = ('id', 'user', 'calendar', 'role')
        read_only_fields = ('id',)
