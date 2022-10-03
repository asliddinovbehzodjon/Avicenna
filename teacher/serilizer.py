from rest_framework import serializers
from .models import FanTest,BlokTestlar
class FanTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FanTest
        fields = "__all__"
class BlokTestlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlokTestlar
        fields = "__all__"