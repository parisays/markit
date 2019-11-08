from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from rest_auth.registration.views import SocialConnectView
from rest_auth.social_serializers import TwitterConnectSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
import tweepy
from users.models import User
from posts.models import Post
from posts.serializers import PostSerializer
from .serializers import (
    SocialAppSerializer,
    SocialTokenSerializer,
)
# from calendars.models import Calendar
# from calendars.serializers import CalendarSerializer
from markit import settings

class TwitterConnect(SocialConnectView):
    """
    Twitter connect view.
    """
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter

class TwitterAppCredential(APIView):
    """
    Get twitter app credentials view.
    """
    serializer_class = SocialAppSerializer
    provider = 'twitter'
    def get(self, request):
        """
        Get method.
        """
        twitter_app = SocialApp.objects.get(provider=self.provider)
        serializer = self.serializer_class(twitter_app)
        return Response(serializer.data)

class TwitterAccountCredential(APIView):
    """
    Get twitter account credentials.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SocialTokenSerializer
    def get(self, request):
        """
        Get user's twitter account credentials.
        """
        user = User.objects.get(email=self.request.user)
        account = SocialAccount.objects.get(user=user)
        social_token = SocialToken.objects.get(account=account)
        serializer = self.serializer_class(social_token)
        return Response(serializer.data)

class TwitterOAuth(APIView):
    """
    Get twitter auth URL.
    """
    provider = 'twitter'
    def get(self, request):
        """
        Get method.
        """
        twitter_app = SocialApp.objects.get(provider=self.provider)
        twitter_auth = tweepy.OAuthHandler(twitter_app.client_id, twitter_app.secret,
                                           settings.TWITTER_CALLBACK_URL)
        twitter_oauth = twitter_auth.get_authorization_url()
        return Response({'url' : twitter_oauth})

class CustomTwitterAccountConnectView(APIView):
    """
    Get twitter authorization tokens.
    """
    permission_classes = (IsAuthenticated,)
    provider = 'twitter'
    def get(self, request, oauth_token, oauth_verifier, calendar_id):
        """
        Get method.
        """
        twitter_app = SocialApp.objects.get(provider=self.provider)
        twitter_auth = tweepy.OAuthHandler(twitter_app.client_id, twitter_app.secret,
                                           settings.TWITTER_CALLBACK_URL)
        twitter_auth.request_token = {'oauth_token' : oauth_token,
                                      'oauth_token_secret' : oauth_verifier}
        twitter_auth.get_access_token(oauth_verifier)
        # return Response({"access_token": twitter_auth.access_token,
        #                  "token_secret": twitter_auth.access_token_secret})
        return self.connect(request, twitter_auth, calendar_id)

    def connect(self, request, twitter_auth, calendar_id):
        """
        Twitter connect.
        """
        token = Token.objects.get(user=request.user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post('/api/v1.0/auth/rest-auth/twitter/connect/', {"access_token": twitter_auth.access_token,
                               "token_secret": twitter_auth.access_token_secret}, format='json')
        return Response(response.data)

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

