from rest_framework import serializers
from . import models
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostsModel
        fields = '__all__'

