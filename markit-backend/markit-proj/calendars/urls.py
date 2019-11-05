from django.conf.urls import url
from calendars.views import (
    CalendarView,
    CalendarListView,
    TweetView,
)

urlpatterns = [
    url(r'^$', CalendarListView.as_view(), name='create-list-calendar'),
    url(r'^(?P<pk>\d+)/$', CalendarView.as_view(), name='detail-calendar'),
    url(r'^tweet/(?P<pk>\d+)/$', TweetView.as_view(), name='tweet-post'),
]
