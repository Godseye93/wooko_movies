from django.contrib.auth.models import AbstractUser
from django.db import models
from movies.models import Genre


class User(AbstractUser):
    # Remove unnecessary fields
    first_name = None
    last_name = None
    date_joined = None
    last_login = None
    is_active = None
    is_staff = None
    is_superuser = None
    
    sex = models.CharField(max_length=20)
    # 프로필 사진
    profile = models.CharField(max_length=200, null=True, blank=True)
    #  팔로워(from_user_id가 팔로우 당한사람 : user_pk)(followings가 팔로우를 한 사람) 목록
    # to_user_id가 팔로우를 신청하면 from_user_id가 팔로우를 당함
    # 즉, to_user_id가 팔로우 신청을 하면
    # to_user_id의 followers(=팔로잉 목록) 목록에 from_user_id가 추가 됨
    # from_user_id의 followings(=팔로워 목록)에 to_user_id가 추가 됨
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    # 좋아하는 장르
    like_genres = models.ManyToManyField(Genre, related_name='like_users', blank=True)