from itertools import chain
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from collaboration.models import Collaborator
from rest_framework.permissions import IsAuthenticated
from calendars.models import Calendar
from calendars.serializers import (
    NestedCalendarSerializer,
    CalendarSerializer,
)
from users.models import User
from .permissions import (
    OwnPermission,
    ManagePermission,
    EditPermission,
    ViewPermission,
)
from collaboration.views import CollaboratorCreateView
from users.serializers import UserAsCollaboratorSerializer

class CalendarListCreateView(generics.ListCreateAPIView):
    """
    Create and list calendars view.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Calendar.objects.all()
    serializer_class = NestedCalendarSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        request.data.update({'owner' : user.id})
        request.data.update({'posts' : []})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # create owner collab
        # collab_view = CollaboratorCreateView.as_view()
        # collab_view(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        own_calendar = Calendar.objects.filter(owner=user)
        # Add calendars that user is a manager/editor/viewer of.
        collab_list = Collaborator.objects.filter(user=user)
        collab_calendar = []
        for collab in collab_list:
            collab_calendar.append(collab.calendar)
        calendar_list = list(chain(own_calendar, collab_calendar))
        serializer = self.get_serializer(calendar_list, many=True)
        return Response(serializer.data)

class CalendarView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve Destroy calendar view.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = NestedCalendarSerializer
    queryset = Calendar.objects.all()

    def update(self, request, *args, **kwargs):
        self.permission_classes = (IsAuthenticated, OwnPermission)
        self.serializer_class = CalendarSerializer
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = (IsAuthenticated, OwnPermission)
        self.serializer_class = NestedCalendarSerializer
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        self.permission_classes = (IsAuthenticated, OwnPermission,
                                   ManagePermission, EditPermission, ViewPermission)
        self.serializer_class = NestedCalendarSerializer
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Append role and access
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar_id=kwargs['pk'])
            access = CollaboratorCreateView.get_role_access(collab.role)
            role = collab.role
        except:
            role = 'Owner'
            access = CollaboratorCreateView.get_role_access(role)
        # Append collaborators
        collab_list = Collaborator.objects.filter(calendar_id=kwargs['pk'])
        collaborators = []
        for collab in collab_list:
            collaborators.append(User.objects.get(email=collab.user))
        collaborators = UserAsCollaboratorSerializer(collaborators, many=True)

        data = {'access' : access, 'role' : role, 'collaborators': collaborators.data}
        data.update(serializer.data)
        return Response(data)

    def check_object_permissions(self, request, obj):
        """
        Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        perms = []
        for permission in self.get_permissions():
            if permission.has_object_permission(request, self, obj):
                perms.append(permission)
        if len(perms) <= 1:
            self.permission_denied(request)