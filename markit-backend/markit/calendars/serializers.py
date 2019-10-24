from calendars.models import Calendar, Post
from users.models import User
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'name', 'text')
        read_only_fields = ('id', )

class CalendarSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=False)

    class Meta:
        model = Calendar
        fields = ('id', 'name', 'posts')
        read_only_fields = ('id', )

    def create(self, validated_data):
        posts_data = validated_data.pop('posts')
        current_calendar = Calendar.objects.create(**validated_data)
        # for post in posts_data:
        #     post, created = Post.objects.get_or_create(name=post['name'])
        #     calendar.posts.add(post)
        # return calendar
        for post in posts_data:
            Post.objects.create(calendar=current_calendar, **post)
        return current_calendar

    def update(self, instance, validated_data):
        posts_data = validated_data.pop('posts')
        # instance.name = validated_data.get('name', instance.name)
        # instance.text = validated_data.get('text', instance.text)
        # instance.description = validated_data.get('description', instance.description)
        # instance.photo = validated_data.get('photo', instance.photo)
        # posts_list = []
        # for post in posts_data:
        #     post, created = Post.objects.get_or_create(name=post["name"])
        #     posts_list.append(post)
        # instance.posts = posts_list
        # instance.save()
        # return instance
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

