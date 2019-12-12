from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
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
    calendar = CalendarSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'firstName', 'lastName', 'calendar')
        read_only_fields = ('id',)


class CustomPasswordResetSerializer(serializers.Serializer):
    """
    Password reset serializer.
    """
    email = serializers.EmailField()
    password_reset_form_class = PasswordResetForm
    def validate_email(self, value):
        """
        Email validator.
        """
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(_('Error'))
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('Invalid e-mail address'))
        return value

    def save(self):
        """
        Save.
        """
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'email_template_name': 'password_reset.txt',
            'request': request,
        }
        self.reset_form.save(**opts)

