from rest_framework import serializers
from collaboration.serializers import CollaboratorSerializer
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    Comment serializer.
    """
    class Meta:
        model = Comment
        fields = ('id', 'post', 'collaborator', 'text', 'reply')
        read_only_fields = ('id', )


class CommentDetailSerializer(serializers.ModelSerializer):
    """
    Comment serializer.
    """
    firstName = serializers.CharField(source='collaborator.user.firstName')
    lastName = serializers.CharField(source='collaborator.user.lastName')
    email = serializers.EmailField(source='collaborator.user.email')
    class Meta:
        model = Comment
        fields = ('id', 'post', 'collaborator', 'firstName', 'lastName',
                  'email', 'text', 'reply')
        read_only_fields = ('id', )
        