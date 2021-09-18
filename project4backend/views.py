from django.shortcuts import render
from .models import User, Task, Reward
from .serializers import UserSerializer, TaskSerializer, RewardSerializer
from rest_framework import viewsets

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RewardView(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer