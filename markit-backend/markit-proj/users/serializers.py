from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.socialaccount.models import SocialApp, SocialToken
from calendars.serializers import CalendarSerializer
from .models import User


class AccountRegistrationSerializer(RegisterSerializer):
    """
    Account registration serializer.
    """
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    firstName = serializers.CharField(required=True)
    lastName = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super(AccountRegistrationSerializer, self).get_cleaned_data()

        return {
            'password': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'firstName': self.validated_data.get('firstName', ''),
            'lastName': self.validated_data.get('lastName', ''),
        }

class CustomAccountDetailsSerializer(serializers.ModelSerializer):
    """
    Custom account detail serializer.
    """
    calendars = CalendarSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('email', 'firstName', 'lastName', 'calendars')

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
