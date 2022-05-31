from django import urls
from rest_framework.routers import DefaultRouter

from .views import TodoModelViewSet

router = DefaultRouter()
router.register(r'', TodoModelViewSet, basename='todo-viewset')

app_name = 'todo'
urlpatterns = [] + router.urls
