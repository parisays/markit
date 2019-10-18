from django.core.mail import send_mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import string
from django.conf import settings
from django.contrib.auth import authenticate
from .models import User


from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    CustomRegisterSerializer,
    CustomUserDetailsSerializer,
    
)

from .serializers import UserSerializer


class SignupAPI(APIView):  # is complete
    permission_classes = (AllowAny,)
    serializer_class = CustomRegisterSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password1']
            firstName = serializer.data['firstName']
            lastName = serializer.data['lastName']
            try:
                user = User.objects.get(email=email)
                if user is Null:
                    content = {'detail':('User with this email already exists.')}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            
            except:
                code = generate_verification_code()
                User.objects.create_user(email=email,
                firstName=firstName, lastName=lastName, password=password)
                send_email(emial_address=email, subject = "Email Verification", 
                           body = 'Your verification code is {}. Please go to this url .'.format(code))
                content = {'email': email, 'firstName': firstName,
                           'lastName': lastName, }

                return Response(content, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignupVerify(APIView):  # not completed
    pass


def generate_verification_code(stringLength=15):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def send_email(emial_address, subject,body):
    fromaddr = settings.EMAIL_HOST_USER
    toaddr = emial_address
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(settings.EMAIL_HOST_USERNAME, settings.EMAIL_HOST_PASSWORD)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


class PasswordResetAPI(APIView):  # complete
    permission_classes = (AllowAny,)
    serializer_class = CustomUserDetailsSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            try:
                user = User.objects.get(email=email)
                if user.verified:
                    password_reset_code = generate_verification_code(40)
                    user.set_password(password_reset_code)
                    user.save()
                    send_email(emial_address=email, subject = "Password Reset ", 
                               body = "Your new password is {}. Please set your new password as soon as possible.".format(password_reset_code))

                    content = {'detail': ('Password reset email sent.')}
                    return Response(content, status=status.HTTP_201_CREATED)

            except:
                pass

            # Since this is AllowAny, don't give away error.
            content = {'detail': ('Password reset not allowed.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class EditProfileAPI(APIView):  # enter blank strings for the fields you dont want to change
                               # is complete
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserDetailsSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            firstName = serializer.data['firstName']
            lastName = serializer.data['lastName']

            user = request.user

            if password != "":
                user.set_password(password)
            else:
                content = {'detail':
                           ('Please enter password.')}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            if user.email != email:
                if email != "" :
                    try:
                        user = User.objects.get(email=email)
                        content = {'detail':
                                   ('User with this email already exists.')}
                        return Response(content, status=status.HTTP_400_BAD_REQUEST)
                    except:
                        user.email = email
                else:
                    content = {'detail':
                               ('Please enter email.')}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

            if firstName != "" :
                user.firstName = firstName
            else:
                content = {'detail':
                           ('Please enter firstName.')}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            if lastName != "" :
                user.lastName = lastName
            else:
                content = {'detail':
                           ('Please enter lastName.')}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            user.save()
            content = {'success': ('Profile edited.')}
            return Response(content, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class UserAPI(APIView): # is complete
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserDetailsSerializer

    def get(self, request, format=None):
        user = User.objects.get(email=request.user.email)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
