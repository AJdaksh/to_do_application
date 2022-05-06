from rest_framework import serializers

from .models import User_Task

class User_Serializer(serializers.Serializer):
    #username = serializers.CharField(max_length=80)
    #email = serializers.EmailField(max_length=100)
    #password=serializers.CharField(max_length=25)
    task_name = serializers.CharField(max_length=80)
    add_on_date = serializers.DateField()
    deadline_date = serializers.DateField()
    status = serializers.CharField(max_length=10)
    user_id = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return User_Task.objects.create(**validated_data)