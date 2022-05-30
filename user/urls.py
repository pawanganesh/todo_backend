from django.urls import path

from .views import (UserRegistrationRequestCreateAPIView, UserLoginRequestAPIView, UserProfileRetrieveUpdateAPIView)

app_name = 'user'
urlpatterns = [
    path('register', UserRegistrationRequestCreateAPIView.as_view(), name='token_obtain_pair'),
    path('login', UserLoginRequestAPIView.as_view(), name="token"),
    path('me', UserProfileRetrieveUpdateAPIView.as_view(), name='current-user'),
]
