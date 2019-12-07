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
        fields = ('id', 'name', 'owner', 'managers', 'editors',
                  'viewers', 'posts', 'connectedPlatforms')
        read_only_fields = ('id', )

class NestedCalendarSerializer(serializers.ModelSerializer):
    """
    Calendar serializer.
    """
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'owner', 'managers', 'editors',
                  'viewers', 'posts', 'connectedPlatforms')
        read_only_fields = ('id', )

    def create(self, validated_data):
        current_calendar = Calendar.objects.create(**validated_data)
        return current_calendar

    def update(self, instance, validated_data):
        manage_data = validated_data.pop('managers')
        edit_data = validated_data.pop('editors')
        view_data = validated_data.pop('viewers')
        current_posts = (instance.posts).all()
        current_posts = list(current_posts)
        instance.name = validated_data.get('name', instance.name)
        instance.connectedPlatforms = validated_data.get('connectedPlatforms',
                                                         instance.connectedPlatforms)

        instance.save()

        for data in manage_data:
            manager = User.objects.filter(email=data)
            instance.managers.add(*manager)

        for data in edit_data:
            editor = User.objects.filter(email=data)
            instance.editors.add(*editor)

        for data in view_data:
            viewer = User.objects.filter(email=data)
            instance.viewers.add(*viewer)

        return instance