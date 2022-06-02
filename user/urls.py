from django.urls import path

from .views import (UserRegistrationRequestCreateAPIView, UserLoginRequestAPIView, UserProfileRetrieveUpdateAPIView)

app_name = 'user'
urlpatterns = [
    path('register', UserRegistrationRequestCreateAPIView.as_view(), name='register'),
    path('login', UserLoginRequestAPIView.as_view(), name="login"),
    path('me', UserProfileRetrieveUpdateAPIView.as_view(), name='current-user'),
]
