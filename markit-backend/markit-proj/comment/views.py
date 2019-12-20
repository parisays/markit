from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import User
from posts.models import Post
from collaboration.models import Collaborator
from .serializers import CommentSerializer
from .models import Comment
from .permissions import CommentPermission, CommentViewPermission

class CommentCreateView(generics.CreateAPIView):
    """
    Create comment view.
    """
    permission_classes = (IsAuthenticated, CommentPermission)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        # check permission
        post = Post.objects.get(pk=request.data['post'])
        self.check_object_permissions(request, post)
        user = User.objects.get(email=self.request.user)
        collaborator = Collaborator.objects.filter(user=user).get(calendar=post.calendar)
        request.data.update({'collaborator' : collaborator.id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CommentListView(generics.ListAPIView):
    """
    List comments view.
    """
    permission_classes = (IsAuthenticated, CommentPermission)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = Post.objects.get(pk=post_id)
        self.check_object_permissions(request, post)
        comment_list = Comment.objects.filter(post_id=post_id)
        serializer = self.get_serializer(comment_list, many=True)
        return Response(serializer.data)

class CommentView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/update/destroy comment view.
    """
    permission_classes = (IsAuthenticated, CommentViewPermission)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    