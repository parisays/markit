from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from calendars.models import Calendar
from .serializers import PostSerializer
from .models import Post
from .permissions import (
    OwnPermission,
    ManagePermission,
    EditPermission,
    ViewPermission,
)

import calendars.permissions as calendar_permissions

class PostCreateView(generics.CreateAPIView):
    """
    Create posts view.
    """
    permission_classes = (IsAuthenticated, OwnPermission, ManagePermission, EditPermission)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostListView(generics.ListAPIView):
    """
    List posts view.
    """
    permission_classes = (IsAuthenticated, calendar_permissions.OwnPermission,
                          calendar_permissions.ManagePermission,
                          calendar_permissions.EditPermission,
                          calendar_permissions.ViewPermission)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        calendar_id = kwargs.get('calendar_id')
        calendar = Calendar.objects.get(id=calendar_id)
        self.check_object_permissions(self.request, calendar)
        post_list = Post.objects.filter(calendar=calendar)
        serializer = self.get_serializer(post_list, many=True)
        return Response(serializer.data)
    
    def check_object_permissions(self, request, obj):
        """
        Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        perms = []
        for permission in self.get_permissions():
            if permission.has_object_permission(request, self, obj):
                perms.append(permission)
        if len(perms) <= 1:
            self.permission_denied(request)


class PostView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve post view.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def retrieve(self, request, *args, **kwargs):
        self.permission_classes = (IsAuthenticated, OwnPermission, ManagePermission,
                                   EditPermission, ViewPermission)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        self.permission_classes = (IsAuthenticated, OwnPermission, ManagePermission,
                                   EditPermission)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = (IsAuthenticated, OwnPermission, ManagePermission,)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def check_object_permissions(self, request, obj):
        """
        Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        perms = []
        for permission in self.get_permissions():
            if permission.has_object_permission(request, self, obj):
                perms.append(permission)
        if len(perms) <= 1:
            self.permission_denied(request)
