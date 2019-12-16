from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from calendars.models import Calendar
from .models import Collaborator, Role
from .serializers import CollaboratorCreateSerializer, RoleSerializer
from .consts import DefienedRoles
from .permissions import CollaboratorPermission

# class RoleCreateView(generics.CreateAPIView):
#     """
#     Create role view.
#     """
#     permission_classes = (IsAuthenticated, )
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CollaboratorCreateView(generics.CreateAPIView):
    """
    Create collaborator view.
    """
    permission_classes = (IsAuthenticated, CollaboratorPermission)
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorCreateSerializer

    def create(self, request, *args, **kwargs):
        calendar = Calendar.objects.get(pk=request.data['calendar'])
        self.check_object_permissions(request, calendar)
        name = request.data.pop('name', 'My Custome Role')
        access = request.data.pop('access', [])
        # check if role is default
        try:
            # use default roles
            role = Role.objects.get(name=name)
        except:
            # create custom role
            access = DefienedRoles.set_role_access(name, access)
            role = Role.objects.create(name=name, access=access)
            role.save()
        request.data.update({'role':role.id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
