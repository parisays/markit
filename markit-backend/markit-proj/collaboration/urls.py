from django.conf.urls import url
from .views import CollaboratorCreateView

urlpatterns = [
    url(r'^$', CollaboratorCreateView.as_view(), name='create-collaborator'),
]