from django.shortcuts import get_object_or_404
from django_celery_beat.models import PeriodicTask
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from notification.models import Invitation
from collaboration.models import Collaborator
from .serializers import InvitationSerializer


@shared_task
def send_invitation_job(invitation_data):
        channel_layer = get_channel_layer()
        invited = invitation_data['invited']
        user_id = get_object_or_404(Collaborator, pk=invited).user.id
        group_name = 'user_{}'.format(str(user_id))
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "notification.notify",
                "data": {
                    'type': 'INVITATION',
                    'calendar': invitation_data['calendar'],
                    'inviter': invitation_data['inviter'],
                    'invited': invitation_data['invited'],
                    'token': invitation_data['token'],
                }
            }
        )
