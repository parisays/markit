from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from calendars.views import *

urlpatterns = [
    url(r'^$', CalendarListView.as_view(), name='create-list-calendar'),
    # url(r'^groups/(?P<calendar_id>[0-9]+)/$', CalendarListView.as_view(), name='calendar_list'),
    url(r'^(?P<pk>\d+)/$', CalendarView.as_view(), name='detail-calendar'),
    url(r'^post/$', PostListView.as_view(), name='create-list-post'),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name='detail-post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
