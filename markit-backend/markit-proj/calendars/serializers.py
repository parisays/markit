from rest_framework import serializers
from rest_auth.registration.serializers import SocialAccountSerializer
from posts.serializers import PostSerializer
from .models import Calendar

class CalendarSerializer(serializers.ModelSerializer):
    """
    Calendar serializer.
    """
    posts = PostSerializer(many=True, read_only=True)
    socials = SocialAccountSerializer(read_only=True)
    class Meta:
        model = Calendar
        fields = ('id', 'name', 'users', 'posts', 'socials')
        read_only_fields = ('id', )
