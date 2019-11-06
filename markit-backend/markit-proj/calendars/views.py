from allauth.socialaccount.models import SocialApp, SocialToken, SocialAccount
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import tweepy
from calendars.models import Calendar
from calendars.serializers import *
from users.models import User
from posts.models import Post
from posts.serializers import PostSerializer


class CalendarListView(generics.ListCreateAPIView):
    """
    Create and list calendars view.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Calendar.objects.all()
    serializer_class = NestedCalendarSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        request.data.update({'owner' : user.id})
        request.data.update({'posts' : []})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        calendar_list = Calendar.objects.filter(owner=user)
        serializer = self.get_serializer(calendar_list, many=True)
        return Response(serializer.data)

class CalendarView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve calendar view.
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = NestedCalendarSerializer
    queryset = Calendar.objects.all()


class TweetView(APIView):
    """
    Tweet on user twitter account.
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = PostSerializer
    provider = 'twitter'

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        twitter_app = SocialApp.objects.get(provider=self.provider)
        user = User.objects.get(email=request.user)
        twitter_account = SocialAccount.objects.get(user=user)
        user_credentials = SocialToken.objects.get(account=twitter_account)
        user_access_token = user_credentials.token
        user_secret_token = user_credentials.token_secret
        twitter_auth = tweepy.OAuthHandler(twitter_app.client_id, twitter_app.secret)
        twitter_auth.set_access_token(user_access_token, user_secret_token)
        twitter_api = tweepy.API(twitter_auth)
        twitter_api.update_status(post.text)

        return Response(True)

