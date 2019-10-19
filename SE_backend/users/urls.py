from django.conf.urls import include, url
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from rest_auth.registration.views import VerifyEmailView, RegisterView
from rest_auth.views import PasswordChangeView, PasswordResetConfirmView, PasswordResetView


urlpatterns = [
    # url(r'^login/$', views.obtain_auth_token),
    url(r'^rest-auth/password_reset/$', PasswordResetView.as_view()),
    re_path(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
             PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/account-confirm-email/(?P<key>.+)/$', VerifyEmailView.as_view()),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
