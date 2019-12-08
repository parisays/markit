from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Collaborator
from .serializers import CollaboratorSerializer
from rest_framework.permissions import IsAuthenticated

class CollaboratorCreateView(generics.CreateAPIView):
    """
    Create collaborator view.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
