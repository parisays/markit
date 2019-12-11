from django.conf.urls import url
from calendars.views import (
    CalendarListCreateView,
    CalendarUpdateView,
    CalendarRetrieveView,
    CalendarDestroyView
)

urlpatterns = [
    url(r'^$', CalendarListCreateView.as_view(), name='create-list-calendar'),
    url(r'^edit/(?P<pk>\d+)/$', CalendarUpdateView.as_view(), name='edit-calendar'),
    url(r'^view/(?P<pk>\d+)/$', CalendarRetrieveView.as_view(), name='view-calendar'),
    url(r'^delete/(?P<pk>\d+)/$', CalendarRetrieveView.as_view(), name='delete-calendar'),
]
