from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from collaboration.permissions import CollaboratorPermission
from .models import Invitation
from .serializers import CalendarInvitationSerializer


class ListCalendarInvitationsView(generics.ListAPIView):
    """
    List calendar invitations view.
    """
    permission_classes = (IsAuthenticated, CollaboratorPermission,)
    serializer_class = CalendarInvitationSerializer
    queryset = Invitation.objects.all()

