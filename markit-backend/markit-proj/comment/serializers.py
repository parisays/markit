from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    Comment serializer.
    """
    class Meta:
        model = Comment
        fields = ('id', 'post', 'collaborator', 'text', 'reply')
        read_only_fields = ('id', )
        # depth = 1
        