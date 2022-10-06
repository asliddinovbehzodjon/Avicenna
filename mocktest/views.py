from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import BotUsers
from .serializer import BotUsersSerializer
class BotUsersViewset(ModelViewSet):
    queryset = BotUsers.objects.all()
    serializer_class = BotUsersSerializer
