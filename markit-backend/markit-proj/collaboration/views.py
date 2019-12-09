from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Collaborator
from .serializers import CollaboratorSerializer
from rest_framework.permissions import IsAuthenticated
from calendars.models import Calendar
from calendars.serializers import CalendarSerializer

ADD_COLLABORATOR = 'A'
DELETE_CALENDAR = 'B'
UPDATE_CALENDAR = 'C'
VIEW_CALENDAR = 'D'
CREATE_POST = 'E'
UPDATE_POST = 'F'
VIEW_POST = 'G'
DELETE_POST = 'H'
POST_COMMENT = 'I'
SET_PUBLISH = 'J'

OWNER = 'Owner'
MANAGER = 'Manager'
EDITOR = 'Editor'
VIEWER = 'Viewer'

class CollaboratorCreateView(generics.ListCreateAPIView):
    """
    Create collaborator view.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer

    def create(self, request, *args, **kwargs):
        # role = request.data['role']
        # access = self.get_role_access(role)
        # request.data.update({'access': access})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @classmethod
    def get_role_access(cls, role):
        """
        Get access for each role.
        """
        switcher = {OWNER : [ADD_COLLABORATOR, DELETE_CALENDAR, UPDATE_CALENDAR, VIEW_CALENDAR,
                             CREATE_POST, UPDATE_POST, VIEW_POST, DELETE_POST, POST_COMMENT,
                             SET_PUBLISH],
                    MANAGER : [VIEW_CALENDAR, CREATE_POST, UPDATE_POST, VIEW_POST,
                               DELETE_POST, POST_COMMENT, SET_PUBLISH],
                    EDITOR : [ADD_COLLABORATOR, DELETE_CALENDAR, UPDATE_CALENDAR,
                              VIEW_CALENDAR, CREATE_POST, UPDATE_POST, VIEW_POST,
                              DELETE_POST, POST_COMMENT],
                    VIEWER : [VIEW_CALENDAR, VIEW_POST, POST_COMMENT]
                    }

        return switcher.get(role, "")
