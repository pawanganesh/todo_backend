from rest_framework.generics import CreateAPIView

from .models import Todo
from .serializers import CreateTodoSerializer


class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = CreateTodoSerializer