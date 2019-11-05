from django.conf.urls import url
from .views import (
    PostView,
    PostListView,
)

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='create-list-post'),
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name='detail-post'),
]
