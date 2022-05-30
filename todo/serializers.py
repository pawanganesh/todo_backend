from rest_framework import serializers
import base64

from .models import Todo


class CreateTodoSerializer(serializers.ModelSerializer):
    todo_image = serializers.ImageField(write_only=True)

    class Meta:
        model = Todo
        fields = ('name', 'todo_image', 'description', 'deadline', 'image')
        read_only_fields = ('image',)
        extra_fields = ['todo_image']
    
    def create(self, validated_data):
        todo_image = validated_data.pop('todo_image')
        format = todo_image.name.split('.')[-1]
        encoded_string = base64.b64encode(todo_image.read())
        validated_data['image'] = "data:image/{};base64,{}".format(format, encoded_string.decode())
        todo = Todo.objects.create(**validated_data, user_id=1)
        return todo

