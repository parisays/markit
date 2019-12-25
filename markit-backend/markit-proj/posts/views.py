from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from calendars.models import Calendar
from socials.tasks import create_tweet_task
from .serializers import PostSerializer
from .models import Post
from .permissions import (
    CreatePostPermission,
    # UpdatePostPermission,
    # DestroyPostPermission,
    # RetrievePostPermission,
    PostPermission,
)

class PostCreateView(generics.CreateAPIView):
    """
    Create posts view.
    """
    permission_classes = (IsAuthenticated, CreatePostPermission)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        # check permission
        calendar = Calendar.objects.get(pk=request.data['calendar'])
        self.check_object_permissions(request, calendar)
        # create post
        data_query_dict = request.data.copy()
        data_query_dict.update({'comments' : []})
        if 'publishDateTime' in data_query_dict:
            data_query_dict.update({'status' : 'Scheduled'})
        serializer = self.get_serializer(data=data_query_dict)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if serializer.data['status'] == 'Scheduled':
            create_tweet_task(serializer.data['id'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PostListView(generics.ListAPIView):
    """
    List posts view.
    """
    permission_classes = (IsAuthenticated, PostPermission)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        calendar_id = kwargs.get('calendar_id')
        calendar = Calendar.objects.get(id=calendar_id)
        post_list = Post.objects.filter(calendar=calendar)
        for post in post_list:
            self.check_object_permissions(request, post)
        serializer = self.get_serializer(post_list, many=True)
        return Response(serializer.data)

class PostUpdateView(generics.UpdateAPIView):
    """
    Update post view.
    """
    permission_classes = (IsAuthenticated, PostPermission)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDestroyView(generics.DestroyAPIView):
    """
    Destroy post view.
    """
    permission_classes = (IsAuthenticated, PostPermission)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostRetrieveView(generics.RetrieveAPIView):
    """
    Destroy post view.
    """
    permission_classes = (IsAuthenticated, PostPermission)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
