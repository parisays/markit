from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from calendars.models import Calendar
from users.models import User
from notification.serializers import InvitationSerializer
from notification.models import Invitation
from notification.tasks import send_invitation_job
from .models import Collaborator, Role
from .serializers import CollaboratorSerializer, RoleSerializer
from .consts import Access, DefienedRoles
from .permissions import InviteCollaboratorPermission

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
    permission_classes = (IsAuthenticated, InviteCollaboratorPermission)
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer

    def create(self, request, *args, **kwargs):
        calendar = Calendar.objects.get(pk=request.data['calendar'])
        self.check_object_permissions(request, calendar)
        user = User.objects.get(email=request.data['email'])
        role_name = request.data.pop('role_name', 'My Custom Role')
        access = request.data.pop('access', [])
        # check if role is default
        try:
            # use default roles
            role = Role.objects.get(name=role_name)
        except:
            # create custom role
            access = DefienedRoles.set_role_access(role_name, access)
            role = Role.objects.create(name=role_name, access=access)
            role.save()
        serializer_data = {'user':user.id, 'role':role.id, 'calendar':calendar.id}
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.create_invitation(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def create_invitation(self, collaborater_data):
        inviter = Collaborator.objects.get(user__email=self.request.user, calendar=collaborater_data['calendar'])
        invitation_data = {'calendar': collaborater_data['calendar'], 'inviter':inviter.id,
                           'invited':collaborater_data['id']}
        serializer = InvitationSerializer(data=invitation_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        send_invitation_job.delay(serializer.data)
