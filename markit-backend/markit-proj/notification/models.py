from uuid import uuid4
from django.db import models
from calendars.models import Calendar
from posts.models import Post
from users.models import User
from collaboration.models import Collaborator
from comment.models import Comment


class Notification(models.Model):
    created = models.DateTimeField(auto_now=True)
    seen = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Invitation(Notification):
    token = models.CharField(max_length=255, null=True)
    calendar = models.ForeignKey(Calendar,
                                 on_delete=models.CASCADE, related_name='calendar_invitations')
    invited = models.ForeignKey(Collaborator,
                                on_delete=models.CASCADE, related_name='user_invitations')
    inviter = models.ForeignKey(Collaborator,
                                on_delete=models.CASCADE, related_name='collaborator_invitations')
    
    def save(self, *args, **kwargs):
        while True:
            try:
                if not self.token:
                    self.token = uuid4().hex
                return super(Invitation, self).save(*args, **kwargs)
            except:
                continue


class PostNotification(Notification):
    editor = models.ForeignKey(Collaborator,
                                 on_delete=models.CASCADE, related_name='collaborator_post_notifications')
    calendar = models.ForeignKey(Calendar,
                                 on_delete=models.CASCADE, related_name='calendar_post_notifications')
    post = models.ForeignKey(Post,
                                 on_delete=models.CASCADE, related_name='post_notifications')


class CommentNotification(Notification):
    calendar = models.ForeignKey(Calendar,
                                 on_delete=models.CASCADE, related_name='calendar_post_comment_notifications')
    post = models.ForeignKey(Post,
                                 on_delete=models.CASCADE, related_name='post_comment_notifications')
    comment = models.ForeignKey(Comment,
                                 on_delete=models.CASCADE, related_name='comment_notifications')