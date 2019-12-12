from django.conf.urls import url
from .views import (CollaboratorCreateView,
                    #  RoleCreateView
                     )

urlpatterns = [
    url(r'^$', CollaboratorCreateView.as_view(), name='create-collaborator'),
    # url(r'^role/$', RoleCreateView.as_view(), name='create-role'),
]
