from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from calendars.models import Calendar
from users.models import User
from notification.serializers import InvitationSerializer
from notification.models import Invitation
from notification.tasks import send_invitation_job
from .models import Collaborator, Role
from .serializers import CollaboratorCreateSerializer, RoleSerializer
from .consts import DefinedRoles
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

    def create_invitation(self, collaborator_data):
        calendar = get_object_or_404(Calendar, pk=collaborator_data['calendar'])
        inviter = get_object_or_404(Collaborator, user__email=self.request.user, calendar=calendar)
        invited = get_object_or_404(Collaborator, pk=collaborator_data['id'])
        invitation = Invitation(calendar=calendar, inviter=inviter,
                           invited=invited)
        invitation.save()
        send_invitation_job.delay(InvitationSerializer(invitation).data)


class ActivateCollaborator(APIView):
    permission_classes = (IsAuthenticated, CollaboratorPermission)

    def post(self, request, token):
        invitation = get_object_or_404(Invitation, token=token)
        invited = invitation.invited
        invited.isConfirmed = True
        invited.save()
        invitation.delete()
        return Response("Collaborator activated successfully", status=status.HTTP_200_OK)


