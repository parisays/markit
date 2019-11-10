from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_auth.registration.views import (
    SocialAccountListView,
    SocialAccountDisconnectView,
)
from .views import (
    TwitterConnect,
    TwitterAccountCredential,
    TwitterOAuth,
    CustomTwitterAccountConnectView,
    TweetView,
    TwitterTrendsView
)


urlpatterns = [
    url(r'^$', SocialAccountListView.as_view(), name='social_account_list'),
    url(r'^(?P<pk>\d+)/disconnect/$',
        SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),
    url(r'^twitter/(?P<calendar_id>\d+)/$', TwitterAccountCredential.as_view(), name='calendar-twitter-account-tokens'),
    url(r'^twitter/oauth$', TwitterOAuth.as_view(), name='twitter-account-oauth'),
    url(r'^twitter/connect/(?P<oauth_token>[\w-]+)/(?P<oauth_verifier>[\w-]+)/(?P<calendar_id>\d+)/$',
        CustomTwitterAccountConnectView.as_view(), name='twitter-account-connect'),
    url(r'^rest-auth/twitter/connect/$', TwitterConnect.as_view(), name='twitter-rest-auth-connect'),
    url(r'^twitter/tweet/(?P<pk>\d+)/$', TweetView.as_view(), name='tweet-post'),
    url(r'^twitter/trends/$', TwitterTrendsView.as_view(), name='twitter-trends'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
