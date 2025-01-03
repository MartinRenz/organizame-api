from rest_framework import serializers
from .models import Task

# Serializer para o modelo de tarefas.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'date', 'is_completed']

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task