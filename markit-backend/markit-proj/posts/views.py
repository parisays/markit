from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from users.models import User
from calendars.models import Calendar
from .serializers import PostSerializer
from .models import Post

class PostListView(generics.ListCreateAPIView):
    """
    Create and list posts view.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        print("before get serializer : ", request.data)
        serializer = self.get_serializer(data=request.data)
        print("before validation")
        serializer.is_valid(raise_exception=True)
        print("before creation")
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        calendar_id = kwargs.get('calendar_id')
        calendar = Calendar.objects.get(id=calendar_id)
        post_list = Post.objects.filter(calendar=calendar)
        serializer = self.get_serializer(post_list, many=True)
        return Response(serializer.data)


class PostView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve post view.
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = PostSerializer
    queryset = Post.objects.all()
