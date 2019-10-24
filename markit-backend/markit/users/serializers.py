from .models import User
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from calendars.models import Calendar
from calendars.serializers import CalendarSerializer

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
    calendars = CalendarSerializer(many=True)
    class Meta:
        model = User
        fields = ('email', 'firstName', 'lastName')
