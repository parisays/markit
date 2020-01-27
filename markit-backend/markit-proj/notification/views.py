from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from collaboration.permissions import CollaboratorPermission
from .models import (
    Invitation,
    PostNotification,
    CommentNotification,
)
from .serializers import CalendarInvitationSerializer


class ListCalendarInvitationsView(generics.ListAPIView):
    """
    List calendar invitations view.
    """
    permission_classes = (IsAuthenticated, CollaboratorPermission,)
    serializer_class = CalendarInvitationSerializer
    queryset = Invitation.objects.all()


class SeenNotificationView(APIView):
    """
    Seen notification.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        try:
            notification = Invitation.objects.get(pk=pk)
        except:
            try:
                notification = PostNotification.objects.get(pk=pk)
            except:
                notification = get_object_or_404(CommentNotification, pk=pk)
                
        notification.seen = True
        notification.save()
        return Response("Notification seen successfully", status=status.HTTP_200_OK)



