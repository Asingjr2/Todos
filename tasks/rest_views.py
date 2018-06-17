from django.contrib.auth.models import User

from rest_framework import viewsets, status, generics
from rest_framework.authentication import  TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import list_route

from rest_framework.generics import GenericAPIView

from apis.serializers import UserSerializer, TaskSerializer, CategorySerializer
from .models import Task, Category


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CustomObtainAuthToken(ObtainAuthToken):
     def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many= False)
        return Response({
            "token": token.key, "user": serializer.data
        })
