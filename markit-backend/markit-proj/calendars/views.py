from allauth.socialaccount.models import SocialApp, SocialToken, SocialAccount
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import tweepy
from calendars.models import *
from calendars.serializers import *
from users.views import TwitterAppCredential
from posts.models import Post


class CalendarView(APIView):
    """
    Get Calendar details.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = CalendarSerializer

    def get(self, request, pk):
        calendar = Calendar.objects.get(id=pk)
        serializer = self.serializer_class(calendar)
        return Response(serializer.data)

class TweetView(APIView):
    """
    Tweet on user twitter account.
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = PostSerializer
    provider = 'twitter'
    def get(self, request, pk):
        """
        Post method.
        """
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

