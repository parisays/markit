from django.conf.urls import url
from .views import PostView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostView.as_view(), name='detail-post'),
]
