import os
import requests
import tweepy
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, status, mixins
from markit import settings
from calendars.models import Calendar
from posts.models import Post
from posts.serializers import PostSerializer
from .serializers import SocialAccountSerializer
from .models import SocialAccount, SocialApp

# class SocialAppCredentials(APIView):
#     """
#     Get twitter app credentials view.
#     """
#     serializer_class = SocialAppSerializer
#     def get(self, request):
#         """
#         Get method.
#         """
#         twitter_app = SocialApp.objects.get(provider='Twitter')
#         serializer = self.serializer_class(twitter_app)
#         return Response(serializer.data)

# class SocialAccountCredential(generics.RetrieveDestroyAPIView):
#     """
#     Social account retreive destroy api view.
#     """
#     permission_classes = (IsAuthenticated,)
#     queryset = SocialAccount.objects.all()
#     serializer_class = SocialAccountSerializer

class TwitterOAuth(APIView):
    """
    Get twitter oauth URL.
    """
    def get(self, request):
        """
        Get method.
        """
        twitter_app = SocialApp.objects.get(provider='Twitter')
        twitter_auth = tweepy.OAuthHandler(twitter_app.clientId, twitter_app.secret,
                                           settings.TWITTER_CALLBACK_URL)
        twitter_oauth = twitter_auth.get_authorization_url()
        return Response({'url' : twitter_oauth})

class TwitterAccountConnect(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    Social account create view.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SocialAccountSerializer
    def get(self, request, *args, **kwargs):
        """
        Get method.
        """
        oauth_token = kwargs.get('oauth_token')
        oauth_verifier = kwargs.get('oauth_verifier')
        twitter_app = SocialApp.objects.get(provider='Twitter')
        twitter_auth = tweepy.OAuthHandler(twitter_app.clientId, twitter_app.secret,
                                           settings.TWITTER_CALLBACK_URL)
        twitter_auth.request_token = {'oauth_token' : oauth_token,
                                      'oauth_token_secret' : oauth_verifier}
        twitter_auth.get_access_token(oauth_verifier)
        calendar_id = kwargs.get('calendar_id')
        calendar = Calendar.objects.get(pk=calendar_id)
        access_token = twitter_auth.access_token
        token_secret = twitter_auth.access_token_secret

        social_account = SocialAccount(app=twitter_app, calendar=calendar, provider='Twitter',
                                       token=access_token, tokenSecret=token_secret)
        serializer = self.serializer_class(data=self.serializer_class(social_account).data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            calendar.connectedPlatforms = 'Twitter'
            calendar.save()
            return Response('twitter account connected to calendar successfully.',
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Tweet(APIView):
    """
    Tweet on user twitter account.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post.status == 'Published':
            return Response("Tweet has been published previously.",
                            status=status.HTTP_400_BAD_REQUEST)
        user = self.request.user
        calendar = Calendar.objects.get(pk=post.calendar.id, owner=user)
        twitter_account = SocialAccount.objects.get(calendar=calendar)
        access_token = twitter_account.token
        secret_token = twitter_account.tokenSecret
        twitter_app = twitter_account.app
        auth = tweepy.OAuthHandler(twitter_app.clientId, twitter_app.secret)
        auth.set_access_token(access_token, secret_token)
        twitter_api = tweepy.API(auth)
        image_url = request.build_absolute_uri(PostSerializer(post).data['image'])
        image_file = 'temp.jpg'
        request = requests.get(image_url, stream=True)
        if request.status_code == 200:
            with open(image_file, 'wb') as image:
                for chunk in request:
                    image.write(chunk)
            twitter_api.update_with_media(image_file, status=post.text)
            os.remove(image_file)
        else:
            twitter_api.update_status(post.text)
        post.status = 'Published'
        post.save()
        return Response("Tweet sent successfully.", status=status.HTTP_200_OK)


class TwitterTrends(APIView):
    """
    Get twitter trends.
    """
    def get(self, request):
        twitter_app = SocialApp.objects.get(provider='Twitter')
        auth = tweepy.OAuthHandler(twitter_app.clientId, twitter_app.secret)
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
