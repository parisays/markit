from django.conf.urls import url
from .views import (
    CommentView,
    CommentCreateView,
    CommentListView,
    CommentUpdateView,
)

urlpatterns = [
    url(r'^$', CommentCreateView.as_view(), name='create-comment'),
    url(r'^list/(?P<post_id>\d+)/$', CommentListView.as_view(), name='list-coment'),
    url(r'^detail/(?P<pk>\d+)/$', CommentView.as_view(), name='detail-comment'),
    url(r'^edit/(?P<pk>\d+)/$', CommentUpdateView.as_view(), name='edit-comment'),
]
