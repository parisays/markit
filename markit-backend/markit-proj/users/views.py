from rest_auth.registration.views import RegisterView, LoginView
from .serializers import (
    CustomAccountDetailsSerializer,
    AccountRegistrationSerializer,
)
from .models import User


class CustomLoginView(LoginView):
    """
    Custom login view.
    """
    def get_response(self):
        response = super().get_response()
        user = User.objects.get(email=self.request.user)
        user_data = CustomAccountDetailsSerializer(user).data
        response.data.update(user_data)
        return response

class CustomRegistrationView(RegisterView):
    """
    Custom registration view.
    """
    serializer_class = AccountRegistrationSerializer
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(email=request.data['email'])
        user_data = CustomAccountDetailsSerializer(user).data
        response.data.update(user_data)
        return response
