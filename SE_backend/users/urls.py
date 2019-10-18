from django.conf.urls import include, url
from rest_framework import routers
from users.views import SignupAPI, LogoutAPI, UserAPI, PasswordResetAPI, EditProfileAPI
from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings

# router = routers.DefaultRouter()

urlpatterns = [
    url(r'^login/$', views.obtain_auth_token),
    url(r'^sign-up/$', SignupAPI.as_view()),
    url(r'^logout/$', LogoutAPI.as_view()),
    url(r'^me/$', UserAPI.as_view()),
    url(r'^PasswordResetAPI/$', PasswordResetAPI.as_view()),
    url(r'^edit-profile/$', EditProfileAPI.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
