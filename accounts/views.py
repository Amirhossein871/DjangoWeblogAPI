from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from . import serializers
# Create your views here.

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
