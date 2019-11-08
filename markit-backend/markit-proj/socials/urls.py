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
)


urlpatterns = [
    url(r'^$', SocialAccountListView.as_view(), name='social_account_list'),
    url(r'^(?P<pk>\d+)/disconnect/$',
        SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),
    url(r'^twitter/user/$', TwitterAccountCredential.as_view(), name='user-social-account-tokens'),
    url(r'^twitter/oauthurl$', TwitterOAuth.as_view(), name='twitter-account-oauth'),
    url(r'^twitter/connect/(?P<oauth_token>[\w-]+)/(?P<oauth_verifier>[\w-]+)/(?P<calendar_id>\d+)/$',
        CustomTwitterAccountConnectView.as_view(), name='twitter-account-connect'),
    url(r'^twitter/rest-auth/connect/$', TwitterConnect.as_view(), name='twitter-rest-auth-connect'),
    url(r'^twitter/tweet/(?P<pk>\d+)/$', TweetView.as_view(), name='tweet-post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
