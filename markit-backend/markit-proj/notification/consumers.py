from channels.generic.websocket import AsyncJsonWebsocketConsumer
from rest_framework.authtoken.models import Token
import json
from calendars.models import Calendar
from collaboration.models import Collaborator
from .tasks import send_all_notifications


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        try:
            token = self.scope.get('url_route', {}).get(
                'kwargs', {}).get('token', False)
            if not token:
                await self.close()
            try:
                token = Token.objects.select_related('user').get(key=token)
            except Token.DoesNotExist:
                await self.close()

            user = token.user
            self.user_group_name = 'user_{}'.format(user.id)

            await self.channel_layer.group_add(
                self.user_group_name,
                self.channel_name,
            )

            calendars = Calendar.objects.filter(collaborator_calendar__user__pk=user.id)
            for calendar in calendars:
                self.calendar_group_name = 'calendar_{}'.format(calendar.id)
                await self.channel_layer.group_add(
                    self.calendar_group_name,
                    self.channel_name,
                )

            send_all_notifications(user, calendars)
            await self.accept()
            

        except Exception as e:
            await self.close()

    async def notification_notify(self, event):
        """
        Notifying business.
        """
        await self.send_json(event["data"])

    async def disconnect(self, close_code):
        """
        WS disconnect.
        """
        await self.channel_layer.group_discard(
            self.user_group_name,
            self.channel_name
        )

    async def receive_json(self, content, **kwargs):
        """
        Receive business.
        """

        serializer = self.get_serializer(data=content)
        if not serializer.is_valid():
            return
        group_name = serializer.get_group_name()
        self.groups.append(group_name)
        await self.channel_layer.group_add(
            group_name,
            self.channel_name,
        )