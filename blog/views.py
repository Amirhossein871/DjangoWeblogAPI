from django.shortcuts import render
from rest_framework import generics
from . import serializers, permissions, models


# Create your views here.
class PostListCreateGenericAPIView(generics.ListCreateAPIView):
    queryset = models.PostsModel.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAdminPermission]

    def perform_create(self, serializer):
        serializer.save()


class PostDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PostsModel.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAdminPermission]
