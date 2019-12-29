from django.conf.urls import url
from .views import (
    CommentView,
    CommentCreateView,
    CommentListView,
)

urlpatterns = [
    url(r'^$', CommentCreateView.as_view(), name='create-comment'),
    url(r'^(?P<post_id>\d+)/$', CommentListView.as_view(), name='list-coment'),
    url(r'^(?P<pk>\d+)/$', CommentView.as_view(), name='detail-comment'),
]
