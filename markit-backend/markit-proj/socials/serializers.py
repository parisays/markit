from rest_framework import serializers
from .models import SocialApp, SocialAccount

class SocialAppSerializer(serializers.ModelSerializer):
    """
    Social app serializer.
    """
    class Meta:
        model = SocialApp
        fields = ('provider', 'clientId', 'secret')

class SocialAccountSerializer(serializers.ModelSerializer):
    """
    Social token serializer.
    """
    class Meta:
        model = SocialAccount
        fields = ('app', 'provider', 'calendar', 'token', 'tokenSecret', 'expireDate')

    def create(self, validated_data):
        return SocialAccount.objects.create(**validated_data)
