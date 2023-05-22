from rest_framework import serializers

from .models import User


# 팔로우 등록 및 해제 : 팔로우 수까지
class FollowSerializer(serializers.ModelSerializer):
    followings = serializers.SerializerMethodField()

    def get_followings(self, obj):
        followings = obj.followings.all()
        return UserSerializer(followings, many=True).data

    class Meta:
        model = User
        fields = ('id', 'username', 'followings')


# 싹다 넣음
class UserSerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    followings = serializers.SerializerMethodField()

    def get_follower_count(self, obj):
        return obj.followings.count()

    def get_followings(self, obj):
        followings = obj.followings.all()
        return FollowSerializer(followings, many=True).data

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'sex', 'profile', 'followings', 'like_genres', 'follower_count')
