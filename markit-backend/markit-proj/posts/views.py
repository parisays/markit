from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from calendars.models import Calendar
from collaboration.models import Collaborator
from users.models import User
from socials.tasks import create_tweet_task
from notification.tasks import create_post_notification_task
from .serializers import PostSerializer
from .models import Post
from .permissions import (
    CreatePostPermission,
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
            create_tweet_task.delay(serializer.data['id'])
        # create_post_notification_task.delay(serializer.data)
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
        if post_list.count() > 0:
            self.check_object_permissions(request, post_list[0])
        # for post in post_list:
        #     self.check_object_permissions(request, post)
        serializer = self.get_serializer(post_list, many=True)
        return Response(serializer.data)

class PostUpdateView(generics.UpdateAPIView):
    """
    Update post view.
    """
    permission_classes = (IsAuthenticated, PostPermission)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        post_notification_data = serializer.data.copy()
        post_notification_data['user'] = self.request.user.id
        create_post_notification_task.delay(post_notification_data)
        return Response(serializer.data)

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

class PostDashboardView(generics.ListAPIView):
    """
    Dashboard posts view.
    """
    permission_classes = (IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        collab_list = Collaborator.objects.filter(user=user)
        draft = 0
        scheduled = 0
        published = 0
        for collab in collab_list:
            post_list = Post.objects.filter(calendar=collab.calendar)
            draft += post_list.filter(status='Draft').count()
            scheduled += post_list.filter(status='Scheduled').count()
            published += post_list.filter(status='Published').count()
        data = {'Draft': draft, 'Scheduled': scheduled, 'Published': published}
        return Response(data)
