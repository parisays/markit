from rest_framework import serializers
from .models import Post
from .Base64Image import Base64ImageField
from comment.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer.
    """
    image = Base64ImageField(max_length=None, use_url=True, required=False)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'calendar', 'subject', 'text', 'status', 'image', 'comments', 'publishDateTime')
        read_only_fields = ('id', )

    def create(self, validated_data):
        current_post = Post.objects.create(**validated_data)
        return current_post

    def update(self, instance, validated_data):
        current_comments = (instance.comments).all()
        current_comments = list(current_comments)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.calendar = validated_data.get('calendar', instance.calendar)
        instance.text = validated_data.get('text', instance.text)
        instance.status = validated_data.get('status', instance.status)
        instance.image = validated_data.get('image', instance.image)

        instance.save()
        return instance
