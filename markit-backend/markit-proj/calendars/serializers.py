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
        fields = ('name', 'user', 'posts')
        read_only_fields = ('id', )
