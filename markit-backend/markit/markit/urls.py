from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from allauth.account.views import confirm_email as allauthemailconfirmation
from django.conf.urls.static import static
from django.conf import settings

urlpatterns  = [
  path('admin/', admin.site.urls),
  path('api/v1.0/auth/', include('users.urls')),
  path('api/v1.0/calendar/', include('calendars.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

