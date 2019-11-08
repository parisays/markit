from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from rest_auth.registration.views import SocialConnectView, RegisterView, LoginView
from rest_auth.social_serializers import TwitterConnectSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
import tweepy
from calendars.models import Calendar
from calendars.serializers import CalendarSerializer
from markit import settings
from .serializers import (
    CustomAccountDetailsSerializer,
    AccountRegistrationSerializer,
    SocialAppSerializer,
    SocialTokenSerializer,
)
from .models import User


class CustomLoginView(LoginView):
    """
    Custom login view.
    """
    def get_response(self):
        response = super().get_response()
        user = User.objects.get(email=self.request.user)
        user_data = CustomAccountDetailsSerializer(user).data
        response.data.update(user_data)
        return response

class CustomRegistrationView(RegisterView):
    """
    Custom registration view.
    """
    serializer_class = AccountRegistrationSerializer
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(email=request.data['email'])
        user_data = CustomAccountDetailsSerializer(user).data
        response.data.update(user_data)
        return response

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
