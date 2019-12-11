from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Collaborator, Role
from .serializers import CollaboratorSerializer, RoleSerializer
from rest_framework.permissions import IsAuthenticated
from calendars.models import Calendar
from .consts import Access, DefienedRoles
from .permissions import InviteCollaboratorPermission

class RoleCreateView(generics.CreateAPIView):
    """
    Create role view.
    """
    permission_classes = (IsAuthenticated, )
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CollaboratorCreateView(generics.ListCreateAPIView):
    """
    Create collaborator view.
    """
    permission_classes = (IsAuthenticated, InviteCollaboratorPermission,)
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer

    def create(self, request, *args, **kwargs):
        calendar = Calendar.objects.get(pk=request.data['calendar'])
        self.check_object_permissions(request, calendar)
        print("create collab")
        name = request.data.pop('name', 'My Custome Role')
        access = request.data.pop('access', [])
        access = DefienedRoles.set_role_access(name, access)
        role = Role.objects.create(name=name, access=access)
        role.save()
        request.data.update({'role':role.id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
