from rest_framework import serializers
from django_celery_beat.models import ClockedSchedule, PeriodicTask
from .models import Post
from .Base64Image import Base64ImageField
from comment.serializers import CommentDetailSerializer

class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer.
    """
    image = Base64ImageField(max_length=None, use_url=True, required=False)
    comments = CommentDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'calendar', 'subject', 'text', 'status', 'image', 'comments', 'publishDateTime')
        read_only_fields = ('id',)

    def create(self, validated_data):
        current_post = Post.objects.create(**validated_data)
        return current_post

    def update(self, instance, validated_data):
        current_comments = (instance.comments).all()
        current_comments = current_comments.values()
        instance.subject = validated_data.get('subject', instance.subject)
        instance.calendar = validated_data.get('calendar', instance.calendar)
        instance.text = validated_data.get('text', instance.text)
        instance.image = validated_data.get('image', instance.image)
        if instance.status == ('Scheduled' or 'Draft'):
            if 'publishDateTime' in validated_data:
                instance.publishDateTime = validated_data.get('publishDateTime', instance.publishDateTime)
                instance.status = 'Scheduled'
                publish_task = instance.publishTask
                schedule = publish_task.clocked
                if schedule.enabled == True:
                    schedule.clocked_time = instance.publishDateTime
                    schedule.save()
                else:
                    new_schedule = ClockedSchedule(clocked_time=instance.publishDateTime)
                    new_schedule.save()
                    publish_task.clocked = new_schedule
                
                publish_task.enabled = True
                publish_task.one_off = True
                publish_task.save()

        instance.save()
        return instance
