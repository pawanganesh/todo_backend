import base64

from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    todo_image = serializers.ImageField(write_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'name', 'todo_image', 'description', 'deadline', 'image', 'created_at', 'updated_at', 'completed')
        read_only_fields = ('id', 'image', 'created_at', 'updated_at')
        extra_fields = ['todo_image']
    
    def create(self, validated_data):
        todo_image = validated_data.pop('todo_image')
        format = todo_image.name.split('.')[-1]
        encoded_string = base64.b64encode(todo_image.read())
        validated_data['completed'] = False # At the moment, the todo is not completed
        validated_data['image'] = "data:image/{};base64,{}".format(format, encoded_string.decode())
        todo = Todo.objects.create(**validated_data, user=self.context['request'].user)
        return todo
    
    def update(self, instance, validated_data):
        if validated_data.get('todo_image'):
            todo_image = validated_data.pop('todo_image')
            format = todo_image.name.split('.')[-1]
            encoded_string = base64.b64encode(todo_image.read())
            validated_data['image'] = "data:image/{};base64,{}".format(format, encoded_string.decode())
        return super().update(instance, validated_data)
