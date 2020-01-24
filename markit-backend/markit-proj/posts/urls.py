from django.conf.urls import url
from django.conf.urls.static import static
from markit import settings
from .views import (
    PostCreateView,
    PostListView,
    PostRetrieveView,
    PostDestroyView,
    PostUpdateView,
    PostDashboardView,
)

urlpatterns = [
    url(r'^$', PostCreateView.as_view(), name='create-post'),
    url(r'^(?P<calendar_id>\d+)/$', PostListView.as_view(), name='list-calendar-posts'),
    url(r'^edit/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='edit-post'),
    url(r'^view/(?P<pk>\d+)/$', PostRetrieveView.as_view(), name='view-post'),
    url(r'^delete/(?P<pk>\d+)/$', PostDestroyView.as_view(), name='delete-post'),
    url(r'^dashboard/$', PostDashboardView.as_view(), name='dashboard-post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
