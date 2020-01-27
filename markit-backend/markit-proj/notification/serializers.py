from rest_framework import serializers
from .models import (
    Invitation,
    PostNotification,
    CommentNotification,
)


class InvitationSerializer(serializers.ModelSerializer):
    """
    Invitation serializer.
    """
    class Meta:
        model = Invitation
        fields = ('id', 'calendar', 'invited', 'inviter', 'token', 'created',)
        read_only_fields = ('id',)


class NotificationListingCollaboratorField(serializers.RelatedField):
    def to_representation(self, value):
        return value.user.email


class NotificationListingCalendarField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

class NotificationListingPostField(serializers.RelatedField):
    def to_representation(self, value):
        return value.subject

class NotificationListingCommentField(serializers.RelatedField):
    def to_representation(self, value):
        return value.collaborator.user.email


class CalendarInvitationSerializer(serializers.ModelSerializer):
    """
    Calendar Invitation serializer.
    """
    invited = NotificationListingCollaboratorField(read_only=True)
    inviter = NotificationListingCollaboratorField(read_only=True)
    calendar = NotificationListingCalendarField(read_only=True)
    class Meta:
        model = Invitation
        fields = ('id', 'calendar', 'invited', 'inviter',)
        read_only_fields = ('id',)


class NotificationInvitationSerializer(serializers.ModelSerializer):
    """
    Calendar Invitation serializer.
    """
    invited = NotificationListingCollaboratorField(read_only=True)
    inviter = NotificationListingCollaboratorField(read_only=True)
    calendar = NotificationListingCalendarField(read_only=True)
    class Meta:
        model = Invitation
        fields = ('id', 'calendar', 'invited', 'inviter', 'token',)
        read_only_fields = ('id',)


class NotificationPostNotificationSerializer(serializers.ModelSerializer):
    """
    Post notification serializer.
    """
    # calendar = NotificationListingCalendarField(read_only=True)
    # post = NotificationListingPostField(read_only=True)
    # editor = NotificationListingCollaboratorField(read_only=True)
    class Meta:
        model = PostNotification
        fields = ('id', 'calendar', 'post', 'editor',)
        read_only_fields = ('id',)


class NotificationCommentNotificationSerializer(serializers.ModelSerializer):
    """
    Post notification serializer.
    """
    # calendar = NotificationListingCalendarField(read_only=True)
    # post = NotificationListingPostField(read_only=True)
    # comment = NotificationListingCommentField(read_only=True)
    class Meta:
        model = CommentNotification
        fields = ('id', 'calendar', 'post', 'comment',)
        read_only_fields = ('id',)
