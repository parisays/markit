from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from rest_auth.registration.views import SocialConnectView
from rest_auth.social_serializers import TwitterConnectSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
import tweepy
from markit import settings
from users.models import User
from calendars.models import Calendar
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
    def get(self, request, calendar_id):
        """
        Get calendar's twitter account credentials.
        """
        calendar = Calendar.objects.get(pk=calendar_id)
        twitter_id = calendar.twitter.id
        account = SocialAccount.objects.get(pk=twitter_id)
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
        return self.connect(request, twitter_auth, calendar_id)

    def connect(self, request, twitter_auth, calendar_id):
        """
        Twitter connect.
        """
        calendar = Calendar.objects.get(pk=calendar_id)
        token = Token.objects.get(user=request.user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post('/api/v1.0/socials/rest-auth/twitter/connect/',
                               {"access_token": twitter_auth.access_token,
                                "token_secret": twitter_auth.access_token_secret},
                               format='json')
        self.connect_calendar(request, calendar)
        return Response(response.data)

    def connect_calendar(self, request, calendar):
        """
        Twitter calendar connection.
        """
        user = User.objects.get(email=request.user)
        twitter_account = SocialAccount.objects.filter(user=user,
                                                       provider='twitter').order_by('id')[0]
        calendar.twitter = twitter_account
        calendar.connectedPlatforms = 'Twitter'
        calendar.save()
        return True

class TweetView(APIView):
    """
    Tweet on user twitter account.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post.status == 'Published':
            return Response(False)
        calendar = Calendar.objects.get(pk=post.calendar.id)
        twitter_id = calendar.twitter.id
        twitter_account = SocialAccount.objects.get(pk=twitter_id)
        credentials = SocialToken.objects.get(account=twitter_account)
        access_token = credentials.token
        secret_token = credentials.token_secret
        auth = tweepy.OAuthHandler(settings.TWITTER_KEY, settings.TWITTER_SECRET)
        auth.set_access_token(access_token, secret_token)
        twitter_api = tweepy.API(auth)
        twitter_api.update_status(post.text)
        post.status = 'Published'
        post.save()

        return Response(True)

class TwitterTrendsView(APIView):
    """
    Get twitter trends.
    """
    def get(self, request):
        auth = tweepy.OAuthHandler(settings.TWITTER_KEY, settings.TWITTER_SECRET)
        api = tweepy.API(auth)
        trends = api.trends_place(2459115)
        data = trends[0]
        trends_data = data['trends']
        response = []
        for trend in trends_data:
            label = trend['name']
            url = trend['url']
            trend_response = {'type':'twitter', 'label':label, 'text':url}
            response.append(trend_response)
        response = JSONRenderer().render(response)
        return Response(response)
