from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from calendars.models import Calendar
from users.models import User
from notification.serializers import NotificationInvitationSerializer
from notification.models import Invitation
from notification.tasks import send_invitation_job
from .models import Collaborator, Role
from .serializers import CollaboratorCreateSerializer, RoleSerializer, CollaboratorSerializer
from .consts import DefinedRoles
from .permissions import CollaboratorPermission

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
        user = User.objects.get(pk=request.data['user'])
        # check collaborator object duplication
        try:
            collab_duplicate = Collaborator.objects.filter(user=user).get(calendar=calendar)
        except:
            collab_duplicate = None
        if(collab_duplicate is not None):
            return Response({"Collaborator Duplication":
                            "Collaborator with role {0} already exists!".format(collab_duplicate.role)},
                            status=status.HTTP_406_NOT_ACCEPTABLE)

        role_name = request.data.pop('role_name', 'My Custom Role')
        access = request.data.pop('access', [])
        role = self.create_or_set_role(role_name, access)
        serializer_data = {'user':user.id, 'role':role.id, 'calendar':calendar.id}
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.create_invitation(serializer.data)
        response_data = {'role_name':role.name, 'email':user.email, 'calendar':calendar.id}
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    def create_or_set_role(self, role_name, access):
        # check if role is default
        try:
            # use default roles
            role = Role.objects.get(name=role_name)
        except:
            # create custom role
            access = DefinedRoles.set_role_access(role_name, access)
            role = Role.objects.create(name=role_name, access=access)
            role.save()
        return role

    def create_invitation(self, collaborator_data):
        calendar = get_object_or_404(Calendar, pk=collaborator_data['calendar'])
        inviter = get_object_or_404(Collaborator, user__email=self.request.user, calendar=calendar)
        invited = get_object_or_404(Collaborator, pk=collaborator_data['id'])
        invitation = Invitation(calendar=calendar, inviter=inviter,
                           invited=invited)
        invitation.save()
        send_invitation_job.delay(NotificationInvitationSerializer(invitation).data)

class RetreiveCollaboratorView(generics.RetrieveAPIView):
    """
    Retreive collaborator api view.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer

class ActivateCollaborator(APIView):
    permission_classes = (IsAuthenticated, CollaboratorPermission)

    def post(self, request, token):
        invitation = get_object_or_404(Invitation, token=token)
        invited = invitation.invited
        invited.isConfirmed = True
        invited.save()
        invitation.delete()
        return Response("Collaborator activated successfully", status=status.HTTP_200_OK)

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
