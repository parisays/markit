from .models import User
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from calendars.models import Calendar
from calendars.serializers import CalendarSerializer
from allauth.socialaccount.models import SocialApp, SocialToken

class AccountRegistrationSerializer(RegisterSerializer):
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
    calendars = CalendarSerializer(many=True, read_only=False)
    class Meta:
        model = User
        fields = ('email', 'firstName', 'lastName', 'calendars')
    # def update(self, instance, validated_data):
    #     calendars_data = validated_data.pop('calendars')
    #     current_calendars = (instance.calendars).all()
    #     current_calendars = list(current_calendars)
    #     instance.firstName = validated_data.get('fistName', instance.firstName)
    #     instance.lastName = validated_data.get('lastName', instance.lastName)
    #     instance.save()

    #     for cal in calendars_data:
    #         c = current_calendars.pop(0)
    #         c.name = cal.get('name', c.name)
    #         p.save()
    #     return instance

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
