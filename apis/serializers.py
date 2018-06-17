from django.contrib.auth.models import User

from rest_framework import serializers

from tasks.models import Task, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = { "password" : { "write_only": True, "required": True}}


class TaskSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Task 
        fields = ("id", "task_name", "importance", "category")

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Category
        fields = ("id", "cat_name",)