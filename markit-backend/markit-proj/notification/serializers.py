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


class InvitationListingCollaboratorField(serializers.RelatedField):
    def to_representation(self, value):
        return value.user.email


class InvitationListingCalendarField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class CalendarInvitationSerializer(serializers.ModelSerializer):
    """
    Calendar Invitation serializer.
    """
    invited = InvitationListingCollaboratorField(read_only=True)
    inviter = InvitationListingCollaboratorField(read_only=True)
    calendar = InvitationListingCalendarField(read_only=True)
    class Meta:
        model = Invitation
        fields = ('id', 'calendar', 'invited', 'inviter',)
        read_only_fields = ('id',)


class NotificationInvitationSerializer(serializers.ModelSerializer):
    """
    Calendar Invitation serializer.
    """
    invited = InvitationListingCollaboratorField(read_only=True)
    inviter = InvitationListingCollaboratorField(read_only=True)
    calendar = InvitationListingCalendarField(read_only=True)
    class Meta:
        model = Invitation
        fields = ('id', 'calendar', 'invited', 'inviter', 'token',)
        read_only_fields = ('id',)
