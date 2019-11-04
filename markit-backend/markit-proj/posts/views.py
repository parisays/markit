from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from users.models import User
from .serializers import PostSerializer
from .models import Post

class PostView(APIView):
    """
    Get post details.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        # user = User.objects.get(email=self.request.user)
        # if user not in post.calendar.user.data:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
