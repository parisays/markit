from rest_framework import serializers
from allauth.socialaccount.models import SocialApp, SocialToken

class SocialAppSerializer(serializers.ModelSerializer):
    """
    Social app serializer.
    """
    class Meta:
        model = SocialApp
        fields = ('provider', 'client_id', 'secret')

class SocialTokenSerializer(serializers.ModelSerializer):
    """
    Social token serializer.
    """
    class Meta:
        model = SocialToken
        fields = ('token', 'token_secret')
