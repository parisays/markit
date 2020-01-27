from django.urls import path
from django.conf.urls import url
from .views import (
    ListCalendarInvitationsView,
    SeenNotificationView,
)

urlpatterns = [
    url(r'^invitation/(?P<calendar_id>\d+)/$', ListCalendarInvitationsView.as_view(), name='list-calendar-invitations'),
    url(r'^seen/(?P<pk>\d+)/$', SeenNotificationView.as_view(), name='seen-notifications'),
]