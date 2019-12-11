from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentSerializer
from .models import Comment
from users.models import User

class CommentCreateView(generics.CreateAPIView):
    """
    Create comment view.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        request.data.update({'user' : user.id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CommentListView(generics.ListAPIView):
    """
    List comments view.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        comment_list = Comment.objects.filter(post_id=post_id)
        serializer = self.get_serializer(comment_list, many=True)
        return Response(serializer.data)

class CommentView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve/update/destroy comment view.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)