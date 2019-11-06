from rest_framework import serializers
from posts.serializers import PostSerializer
from .models import Calendar

class CalendarSerializer(serializers.ModelSerializer):
    """
    Calendar serializer.
    """
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'owner', 'collaborators', 'posts', 'connected_platforms')
        read_only_fields = ('id', )

class NestedCalendarSerializer(serializers.ModelSerializer):
    """
    Calendar serializer.
    """
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'owner', 'collaborators', 'posts', 'connected_platforms')
        read_only_fields = ('id', )

    def create(self, validated_data):
        # posts_data = validated_data.pop('posts')
        current_calendar = Calendar.objects.create(**validated_data)
        # for post in posts_data:
        #     Post.objects.create(calendar=current_calendar, **post)
        return current_calendar

    def update(self, instance, validated_data):
        posts_data = validated_data.pop('posts')
        current_posts = (instance.posts).all()
        current_posts = list(current_posts)
        instance.name = validated_data.get('name', instance.name)
        instance.collaborators = validated_data.get('collaborators', instance.collaborators)
        instance.connected_platforms = validated_data.get('connected_platforms', instance.connected_platforms)
        instance.save()

        for post in posts_data:
            p = current_posts.pop(0)
            p.name = post.get('subject', p.subject)
            p.text = post.get('text', p.text)
            p.status = post.get('status', p.status)
            p.save()
        return instance