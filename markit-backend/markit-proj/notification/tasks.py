from django.shortcuts import get_object_or_404
from django_celery_beat.models import PeriodicTask
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from collaboration.models import Collaborator
from users.models import User
from calendars.models import Calendar
from posts.models import Post
from comment.models import Comment
from .serializers import (
    NotificationInvitationSerializer,
    NotificationPostNotificationSerializer,
    NotificationCommentNotificationSerializer,
)
from .models import (
    Invitation,
    PostNotification,
    CommentNotification,
)


@shared_task
def send_all_notifications(user, calendars):
    # invitations
    invitations = Invitation.objects.filter(invited__user=user, seen=False)
    for invitation in invitations:
        send_invitation_job.delay(NotificationInvitationSerializer(invitation).data)

    # post notifications
    post_notifications = PostNotification.objects.filter(calendar__in=calendars, seen=False)
    for post_notification in post_notifications:
        send_post_notification_job.delay(NotificationPostNotificationSerializer(post_notification).data)

    # comment notifications
    comment_notifications = CommentNotification.objects.filter(calendar__in=calendars, seen=False)
    for comment_notification in comment_notifications:
        send_comment_notification_job.delay(NotificationCommentNotificationSerializer(comment_notification).data)


@shared_task
def create_invitation_task(collaborator_data):
    calendar = get_object_or_404(Calendar, pk=collaborator_data['calendar'])
    inviter = get_object_or_404(Collaborator, user__email=self.request.user, calendar=calendar)
    invited = get_object_or_404(Collaborator, pk=collaborator_data['id'])
    invitation = Invitation(calendar=calendar, inviter=inviter,
                        invited=invited)
    invitation.save()
    send_invitation_job.delay(NotificationInvitationSerializer(invitation).data)


@shared_task
def send_invitation_job(data):
    channel_layer = get_channel_layer()
    invited = data['invited']
    user_id = get_object_or_404(User, email=invited).id
    group_name = 'user_{}'.format(str(user_id))
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "notification.notify",
            "data": {
                'id': data['id'],
                'type': 'invitation',
                'title': 'New Invitation!',
                'text': '{} has invited you to {} calendar!'.format(data['inviter'], data['calendar']),
                'additionalData': {
                    'token': data['token'],
                }                    
                
            }
        }
    )


@shared_task
def create_post_notification_task(post_data):
    editor = Collaborator.objects.get(calendar=post_data['calendar'], user__pk=post_data['user'])
    calendar = get_object_or_404(Calendar, pk=post_data['calendar'])
    post = get_object_or_404(Post, pk=post_data['id'])
    post_notification = PostNotification(editor=editor, calendar=calendar, post=post)
    post_notification.save()
    send_post_notification_job.delay(NotificationPostNotificationSerializer(post_notification).data)
 


@shared_task
def send_post_notification_job(data):
    channel_layer = get_channel_layer()
    calendar = get_object_or_404(Calendar, pk=data['calendar'])
    post = get_object_or_404(Post, pk=data['post'])
    editor = get_object_or_404(Collaborator, pk=data['editor'])
    group_name = 'calendar_{}'.format(calendar.id)
    print(group_name)
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "notification.notify",
            "data": {
                'id': data['id'],
                'type': 'edit_post',
                'title': 'Post Edit',
                'text': '{} edited {} on {} calendar.'.format(editor.user.email, post.subject, calendar.name),
                'additionalData': {
                    'calendarId': calendar.id,
                    'postId': post.id,
                    'notif_creator': editor.user.email
                }                    
                
            }
        }
    )


@shared_task
def create_comment_notification_task(comment_data):
    post = get_object_or_404(Post, pk=comment_data['post'])
    calendar = post.calendar
    comment = get_object_or_404(Comment, pk=comment_data['id'])
    comment_notification = CommentNotification(calendar=calendar, post=post, comment=comment)
    comment_notification.save()
    send_comment_notification_job.delay(NotificationCommentNotificationSerializer(comment_notification).data)


@shared_task
def send_comment_notification_job(data):
    channel_layer = get_channel_layer()
    calendar = get_object_or_404(Calendar, pk=data['calendar'])
    post = get_object_or_404(Post, pk=data['post'])
    comment = get_object_or_404(Comment, pk=data['comment'])
    editor = comment.collaborator
    group_name = 'calendar_{}'.format(calendar.id)
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "notification.notify",
            "data": {
                'id': data['id'],
                'type': 'comment',
                'title': 'New Comment!',
                'text': '{} commented on {} on {} calendar.'.format(editor.user.email, post.subject, calendar.name),
                'additionalData': {
                    'calendarId': calendar.id,
                    'postId': post.id,
                    'notif_creator': editor.user.email
                }                    
                
            }
        }
    )
