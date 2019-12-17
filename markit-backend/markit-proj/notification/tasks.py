from django_celery_beat.models import PeriodicTask, ClockedSchedule
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from notification.models import Invitation
from .serializers import InvitationSerializer


@shared_task
def send_invitation_job(serializer_data):
        print('start sending invitation...')
        channel_layer = get_channel_layer()
        print('channel layer: {}'.format(channel_layer))
        invitation = Invitation.objects.get(pk=serializer_data['id'])
        user_id = invitation.invited.user.id
        group_name = 'user_{}'.format(user_id)
        print('group name: {}'.format(group_name))
        async_to_sync(channel_layer.group_send)(
            group_name, 
            {
                "type": "notification.notify",
                "data": {
                    'type': 'INVITATION',
                    'calendar': serializer_data['calendar'],
                    'inviter': serializer_data['inviter'],
                    'invited': serializer_data['invited'],
                }
            }
        )
