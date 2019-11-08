from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from rest_auth.registration.views import (
    VerifyEmailView,
    SocialAccountListView,
    SocialAccountDisconnectView,
)
from rest_auth.views import PasswordResetConfirmView, PasswordResetView
from .views import (
    TwitterConnect,
    CustomRegistrationView,
    CustomLoginView,
    TwitterAccountCredential,
    TwitterOAuth,
    CustomTwitterAccountConnectView,
)


urlpatterns = [
    url(r'^rest-auth/password_reset/$', PasswordResetView.as_view()),
    re_path(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^rest-auth/twitter/connect/$', TwitterConnect.as_view(), name='twitter-connect'),
    url(r'^rest-auth/login/$', CustomLoginView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/$', CustomRegistrationView.as_view()),
    url(r'^rest-auth/registration/account-confirm-email/(?P<key>.+)/$', VerifyEmailView.as_view()),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    url(r'^socialaccounts/$', SocialAccountListView.as_view(), name='social_account_list'),
    url(r'^socialaccounts/(?P<pk>\d+)/disconnect/$',
        SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),
    url(r'^user-twitter/$', TwitterAccountCredential.as_view(), name='user-social-account-tokens'),
    url(r'^twitter/oauth$', TwitterOAuth.as_view(), name='twitter-account-oauth'),
    url(r'^twitter/connect/(?P<oauth_token>[\w-]+)/(?P<oauth_verifier>[\w-]+)/(?P<calendar_id>\d+)/$',
        CustomTwitterAccountConnectView.as_view(), name='twitter-account-connect'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
