from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls import path, re_path
from django.conf import settings
from rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/auth/', include('users.urls')),
    path('api/v1.0/calendar/', include('calendars.urls')),
    path('api/v1.0/post/', include('posts.urls')),
    path('api/v1.0/socials/', include('socials.urls')),
    path('api/v1.0/collaboration/', include('collaboration.urls')),
    path('api/v1.0/comment/', include('comment.urls')),
    path('api/v1.0/notification/', include('notification.urls')),
    # password recovery url
    re_path(r'^user/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
