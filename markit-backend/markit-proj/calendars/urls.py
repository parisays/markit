from django.conf.urls import url
from calendars.views import (
    CalendarView,
    CalendarListCreateView,
)

urlpatterns = [
    url(r'^$', CalendarListCreateView.as_view(), name='create-list-calendar'),
    url(r'^(?P<pk>\d+)/$', CalendarView.as_view(), name='detail-calendar'),
]
