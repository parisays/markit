from rest_framework import serializers
from rest_auth.registration.serializers import SocialAccountSerializer
from posts.serializers import PostSerializer
from collaboration.serializers import CollaboratorSerializer
from .models import Calendar

class CalendarSerializer(serializers.ModelSerializer):
    """
    Calendar serializer.
    """
    posts = PostSerializer(many=True, read_only=True)
    collaborator_calendar = CollaboratorSerializer(many=True, read_only=True)
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'owner', 'posts', 'connectedPlatforms', 'collaborator_calendar')
        read_only_fields = ('id', )

class NestedCalendarSerializer(serializers.ModelSerializer):
    """
    Calendar serializer.
    """
    posts = PostSerializer(many=True, read_only=True)
    collaborator_calendar = CollaboratorSerializer(many=True, read_only=True)
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'owner', 'posts', 'connectedPlatforms', 'collaborator_calendar')
        read_only_fields = ('id', )

    def create(self, validated_data):
        current_calendar = Calendar.objects.create(**validated_data)
        return current_calendar

    def update(self, instance, validated_data):
        current_posts = (instance.posts).all()
        current_posts = list(current_posts)
        instance.name = validated_data.get('name', instance.name)
        instance.connectedPlatforms = validated_data.get('connectedPlatforms',
                                                         instance.connectedPlatforms)

        instance.save()
        return instance
        