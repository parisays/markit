from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.registration.views import SocialConnectView
from rest_auth.social_serializers import TwitterConnectSerializer
from .serializers import SocialAppSerializer
from rest_framework import generics
from allauth.socialaccount.models import SocialApp
from rest_framework.response import Response

class TwitterConnect(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter

class TwitterAppAuth(generics.RetrieveAPIView):
    """
    Return twitter app credentials.
    """
    serializer_class = SocialAppSerializer
    lookup_field = 'pk'
    queryset = SocialApp.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object() # here the object is retrieved
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
