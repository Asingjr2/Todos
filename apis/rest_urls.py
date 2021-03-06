from django.urls import path, include

from rest_framework import routers 

from tasks.rest_views import UserViewSet, TaskViewSet, CategoryViewSet, CustomObtainAuthToken

# Urls do not need entering slack since base ends in slash
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns= [
    path("", include(router.urls)), 
    path("authenticate/", CustomObtainAuthToken.as_view()),
    path("api-login/", include("rest_framework.urls")),
]


