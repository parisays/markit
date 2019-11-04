from rest_framework import serializers
from .models import Calendar, Post
from users.models import User

# class CalendarSerializer(serializers.ModelSerializer):

#     class Meta:
#             model = Calendar
#             fields = ('id' , 'name', 'user')
#             read_only_fields = ('id', )


class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer.
    """
    # calendar = CalendarSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'calendar', 'name', 'text')
        read_only_fields = ('id', )

class NestedCalendarSerializer(serializers.ModelSerializer):
    """
    Nested Calendar Serializer
    """
    posts = PostSerializer(many=True, read_only=False)

    class Meta:
        model = Calendar
        fields = ('id' , 'name', 'user', 'posts')
        read_only_fields = ('id', )

    def create(self, validated_data):
        posts_data = validated_data.pop('posts')
        user_data = validated_data.pop('user')
        current_calendar = Calendar.objects.create(**validated_data)

        for post in posts_data:
            Post.objects.create(calendar=current_calendar, **post)

        
        print(current_calendar)
        current_calendar.user.add(*user_data)
        return current_calendar

    def update(self, instance, validated_data):
        posts_data = validated_data.pop('posts')
        current_posts = (instance.posts).all()
        current_posts = list(current_posts)
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        for post in posts_data:
            p = current_posts.pop(0)
            p.name = post.get('name', p.name)
            p.text = post.get('text', p.text)
            p.save()
        return instance

