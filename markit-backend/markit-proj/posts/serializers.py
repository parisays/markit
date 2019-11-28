from rest_framework import serializers
from .models import Post
from .Base64Image import Base64ImageField

class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer.
    """
    image = Base64ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = Post
        fields = ('id', 'calendar', 'subject', 'text', 'status', 'image', 'publishDateTime')
        read_only_fields = ('id', )
