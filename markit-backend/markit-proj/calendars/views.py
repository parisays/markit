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
    UpdateCalendarPermission,
    DestroyCalendarPermission,
    RetrieveCalendarPermission
)
from collaboration.models import Collaborator

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
        # create owner collab
        # owner_collaborator = Collaborator.objects.create(user=user,calendar=,role=)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
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

class CalendarUpdateView(generics.UpdateAPIView):
    """
    Update calendar view.
    """
    permission_classes = (IsAuthenticated, UpdateCalendarPermission,)
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()

class CalendarRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve calendar view.
    """
    permission_classes = (IsAuthenticated, RetrieveCalendarPermission,)
    serializer_class = NestedCalendarSerializer
    queryset = Calendar.objects.all()

class CalendarDestroyView(generics.DestroyAPIView):
    """
    Destroy calendar view.
    """
    permission_classes = (IsAuthenticated, DestroyCalendarPermission,)

    serializer_class = NestedCalendarSerializer
    queryset = Calendar.objects.all()

# class CalendarView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve Destroy Update calendar view.
#     """
#     permission_classes = (IsAuthenticated,)
#     serializer_class = NestedCalendarSerializer
#     queryset = Calendar.objects.all()

#     def update(self, request, *args, **kwargs):
#         self.permission_classes = (IsAuthenticated, OwnPermission)
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         print(serializer)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

#     def destroy(self, request, *args, **kwargs):
#         self.permission_classes = (IsAuthenticated, OwnPermission)
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def retrieve(self, request, *args, **kwargs):
#         self.permission_classes = (IsAuthenticated, OwnPermission,
#                                    ManagePermission, EditPermission, ViewPermission)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     def check_object_permissions(self, request, obj):
#         """
#         Check if the request should be permitted for a given object.
#         Raises an appropriate exception if the request is not permitted.
#         """
#         perms = []
#         for permission in self.get_permissions():
#             if permission.has_object_permission(request, self, obj):
#                 perms.append(permission)
#         if len(perms) <= 1:
#             self.permission_denied(request)


#     def get_serializer_class(self):
#         """
#         Return the class to use for the serializer.
#         Defaults to using `self.serializer_class`.
#         """
#         if self.request.method == 'PUT' or self.request.method == 'PATCH':
#             return CalendarSerializer
#         return self.serializer_class
