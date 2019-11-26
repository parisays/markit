from rest_framework import serializers
from rest_auth.registration.serializers import SocialAccountSerializer
from posts.serializers import PostSerializer
from users.models import User
from .models import Calendar


class CalendarSerializer(serializers.ModelSerializer):
    """
    Calendar serializer.
    """
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'owner', 'collaborators', 'posts', 'connectedPlatforms')
        read_only_fields = ('id', )

class NestedCalendarSerializer(serializers.ModelSerializer):
    """
    Calendar serializer.
    """
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'owner', 'collaborators', 'posts', 'connectedPlatforms')
        read_only_fields = ('id', )

    def create(self, validated_data):
        current_calendar = Calendar.objects.create(**validated_data)
        return current_calendar

    def update(self, instance, validated_data):
        collab_data = validated_data.pop('collaborators')
        current_posts = (instance.posts).all()
        current_posts = list(current_posts)
        instance.name = validated_data.get('name', instance.name)
        instance.connectedPlatforms = validated_data.get('connectedPlatforms',
                                                         instance.connectedPlatforms)

        instance.save()

        for data in collab_data:
            collaborator = User.objects.filter(email=data)
            instance.collaborators.add(*collaborator)

        return instance


class CalendarUpdateSerializer(serializers.ModelSerializer):
    """
    Calendar serializer.
    """
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'owner', 'collaborators', 'connectedPlatforms')
        read_only_fields = ('id', )
