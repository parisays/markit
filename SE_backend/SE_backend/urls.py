from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from allauth.account.views import confirm_email as allauthemailconfirmation
from calendars.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns  = [
  path('admin/', admin.site.urls),
  url(r'^api/calendar/$', CalendarListView.as_view()),
  # url(r'^groups/(?P<calendar_id>[0-9]+)/$', CalendarListView.as_view(), name='calendar_list'),
  url(r'^api/calendar/(?P<pk>\d+)/$', CalendarView.as_view()),
  url(r'^api/post/$', PostListView.as_view()),
  url(r'^api/post/(?P<pk>\d+)/$', PostView.as_view()),
  path('api/auth/v1.0/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
