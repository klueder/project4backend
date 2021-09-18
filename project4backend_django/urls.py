from project4backend.models import User
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from project4backend.views import UserView, TaskView, RewardView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("users", UserView, basename='userview')
route.register("tasks", TaskView, basename='taskview')
route.register("rewards", RewardView, basename='rewardview')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
]
