from django.conf.urls import url
from .views import (CollaboratorCreateView,
                    #  RoleCreateView
                    ActivateCollaborator)

urlpatterns = [
    url(r'^$', CollaboratorCreateView.as_view(), name='create-collaborator'),
    # url(r'^role/$', RoleCreateView.as_view(), name='create-role'),
    url(r'^activate/(?P<token>[\w-]+)$', ActivateCollaborator.as_view(), name='activate-collaborator'),
]
