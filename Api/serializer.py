from rest_framework import serializers
from App.models import TodoList


class TodoAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
