from rest_framework import serializers
from .models import Invitation

class InvitationSerializer(serializers.ModelSerializer):
    """
    Invitation serializer.
    """
    class Meta:
        model = Invitation
        fields = ('id', 'calendar', 'invited', 'inviter', 'token', 'created',)
        read_only_fields = ('id',)
