from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer.
    """
    class Meta:
        model = Post
        fields = ('id', 'calendar', 'subject', 'text', 'status')
        read_only_fields = ('id', )
