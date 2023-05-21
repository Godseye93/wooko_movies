from rest_framework import serializers

from .models import WorldCupItem


class WorldCupItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldCupItem
        fields = ['id', 'name', 'image_url', 'votes']
        # fields = '__all__'
