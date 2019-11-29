from django.conf.urls import url
from django.conf.urls.static import static
from markit import settings
from .views import (
    PostView,
    PostCreateView,
    PostListView,
)

urlpatterns = [
    url(r'^$', PostCreateView.as_view(), name='create-post'),
    url(r'^(?P<calendar_id>\d+)$', PostListView.as_view(), name='list-post'),
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name='detail-post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
