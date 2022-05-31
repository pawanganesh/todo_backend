from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Todo
from .serializers import TodoSerializer


class TodoModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    http_method_names = ['get', 'patch', 'delete', 'post']
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]

    ordering_fields = ['created_at', 'name']
    search_fields = ['name',]
    filterset_fields = ['completed',]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
