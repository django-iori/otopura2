from django.contrib.auth import models
from rest_framework import serializers

from otopuraapp.models import HostModel
from .models import *

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostModel
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

class UploadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandModel
        fields = '__all__'

class GoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodModel
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'

