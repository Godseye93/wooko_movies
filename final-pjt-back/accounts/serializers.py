from rest_framework import serializers

from .models import User


# 싹다 넣음
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'sex',
                  'profile', 'followings', 'like_genres')


# 팔로우 등록 및 해제 : 팔로우 수까지
class FollowSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)

    followings = UserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'followings')