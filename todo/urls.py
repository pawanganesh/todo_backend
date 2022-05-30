from django.urls import path

from .views import (TodoCreateAPIView)

app_name = 'todo'
urlpatterns = [
    path('', TodoCreateAPIView.as_view(), name='create'),
]
