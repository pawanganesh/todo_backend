from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from django.contrib.auth import get_user_model

from .serializers import UserRegistrationRequestSerializer, UserLoginRequestSerializer, UserSerializer

USER = get_user_model()


class UserRegistrationRequestCreateAPIView(CreateAPIView):
    """
    User create
    ```
    {
        "full_name": "Pawan lal Ganesh",
        "email": "pawanlalganesh@gmail.com",
        "password": "Secret@123"
    }
    ```
    """
    permission_classes = [AllowAny, ]
    queryset = USER.objects.all()
    serializer_class = UserRegistrationRequestSerializer


class UserLoginRequestAPIView(APIView):
    """
    User login
    ```
    {
        "email": "pawanlalganesh@gmail.com",
        "password": "Secret@123"
    }
    ```
    """
    permission_classes = [AllowAny, ]

    @staticmethod
    def post(request):
        serializer = UserLoginRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        access_token = AccessToken.for_user(user)
        return Response({
            "access_token": str(access_token),
        })


class UserProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
    User profile
    ```
    {
        "full_name": "Pawanlal Ganesh",
        "email": "pawanlalganesh@gmail.com"
    }
    ```
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']

    def get_object(self):
        return self.request.user
