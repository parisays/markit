from itertools import chain
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from collaboration.consts import DefinedRoles
from collaboration.models import Collaborator, Role
from collaboration.serializers import RoleSerializer
from .models import Calendar
from rest_framework.permissions import IsAuthenticated
from users.models import User
from .serializers import (
    NestedCalendarSerializer,
    CalendarSerializer,
)
from .permissions import (
    # UpdateCalendarPermission,
    # DestroyCalendarPermission,
    # RetrieveCalendarPermission,
    CalendarPermission,
)

class CalendarListCreateView(generics.ListCreateAPIView):
    """
    Create and list calendars view.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Calendar.objects.all()
    serializer_class = NestedCalendarSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        _mutable = request.data._mutable
        # set to mutable
        request.data._mutable = True
        request.data.update({'owner' : user.id})
        request.data.update({'posts' : []})
        # set mutable flag back
        request.data._mutable = _mutable
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # create owner collab
        owner_role = Role.objects.get(name=DefinedRoles.OWNER)
        currunt_calendar = Calendar.objects.get(pk=serializer.data['id'])
        owner_collaborator = Collaborator.objects.create(user=user,
                                                         calendar=currunt_calendar,
                                                         role=owner_role)
        owner_collaborator.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        collab_list = Collaborator.objects.filter(user=user)
        calendar_list = []
        for collab in collab_list:
            calendar_list.append(collab.calendar)
        serializer = self.get_serializer(calendar_list, many=True)
        return Response(serializer.data)

class CalendarUpdateView(generics.UpdateAPIView):
    """
    Update calendar view.
    """
    permission_classes = (IsAuthenticated, CalendarPermission,)
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()

class CalendarRetrieveView(generics.RetrieveAPIView):
    """
    Retrieve calendar view.
    """
    permission_classes = (IsAuthenticated, CalendarPermission,)
    serializer_class = NestedCalendarSerializer
    queryset = Calendar.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # add role access
        collab_obj = Collaborator.objects.filter(user=request.user).get(calendar=instance)
        role_serializer = RoleSerializer(collab_obj.role)
        data = role_serializer.data
        data.update(serializer.data)
        data.update({'role': role_serializer.data['name']})
        return Response(data)

class CalendarDestroyView(generics.DestroyAPIView):
    """
    Destroy calendar view.
    """
    permission_classes = (IsAuthenticated, CalendarPermission,)

    serializer_class = NestedCalendarSerializer
    queryset = Calendar.objects.all()