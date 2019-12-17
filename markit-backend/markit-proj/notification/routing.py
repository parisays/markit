from django.urls import re_path
from .consumers import NotificationConsumer

notification_websocket_urls = [
    re_path(r'^ws/notification/(?P<token>[\w-]+)/$', NotificationConsumer, name='ws_notifications'),
]