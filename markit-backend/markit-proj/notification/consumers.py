from channels.generic.websocket import AsyncJsonWebsocketConsumer
from rest_framework.authtoken.models import Token
import json

class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        try:
            # Pass auth token as a part of url.
            token = self.scope.get('url_route', {}).get(
                'kwargs', {}).get('token', False)
            # If no token specified, close the connection
            if not token:
                await self.close()
            # Try to authenticate the token from DRF's Token model
            try:
                token = Token.objects.select_related('user').get(key=token)
            except Token.DoesNotExist:
                await self.close()

            user = token.user

            # Get the group to which user is to be subscribed.
            self.user_group_name = 'user_{}'.format(user.id)

            # Add this channel to the group.
            await self.channel_layer.group_add(
                self.user_group_name,
                self.channel_name,
            )
            await self.accept()

        except Exception as e:
            await self.close()

    async def notification_notify(self, event):
        """
        This handles calls elsewhere in this codebase that look
        like:

            channel_layer.group_send(group_name, {
                'type': 'notify',  # This routes it to this handler.
                'content': json_message,
            })

        Don't try to directly use send_json or anything; this
        decoupling will help you as things grow.
        """
        print('start notifying...')
        await self.send_json(event["data"])

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.user_group_name,
            self.channel_name
        )

    async def receive_json(self, content, **kwargs):
        """
        This handles data sent over the wire from the client.

        We need to validate that the received data is of the correct
        form. You can do this with a simple DRF serializer.

        We then need to use that validated data to confirm that the
        requesting user (available in self.scope["user"] because of
        the use of channels.auth.AuthMiddlewareStack in routing) is
        allowed to subscribe to the requested object.
        """
        serializer = self.get_serializer(data=content)
        if not serializer.is_valid():
            return
        # Define this method on your serializer:
        group_name = serializer.get_group_name()
        # The AsyncJsonWebsocketConsumer parent class has a
        # self.groups list already. It uses it in cleanup.
        self.groups.append(group_name)
        # This actually subscribes the requesting socket to the
        # named group:
        await self.channel_layer.group_add(
            group_name,
            self.channel_name,
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send_json(content=json.dumps({
            'message': message
        }))