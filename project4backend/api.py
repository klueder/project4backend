from .models import User, Task, Reward
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, TaskSerializer, RewardSerializer

# User Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

# Task Viewset
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TaskSerializer

# Reward Viewset
class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RewardSerializer
