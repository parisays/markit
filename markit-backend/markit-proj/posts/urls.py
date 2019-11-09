from django.conf.urls import url
from django.conf.urls.static import static
from markit import settings
from .views import (
    PostView,
    PostListView,
)

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='create-list-post'),
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name='detail-post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
