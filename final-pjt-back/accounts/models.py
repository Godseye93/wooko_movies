from django.contrib.auth.models import AbstractUser
from django.db import models
from movies.models import Actor, Director, Genre


class User(AbstractUser):
    # Remove unnecessary fields
    first_name = None
    last_name = None
    date_joined = None
    last_login = None
    is_active = True
    is_staff = False
    is_superuser = False
    sex = models.CharField(max_length=20)
    # 프로필 사진
    profile = models.CharField(max_length=200, null=True, blank=True)
    # 팔로윙
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    # 좋아하는 장르
    liked_genres = models.ManyToManyField(Genre, related_name='like_users', blank=True)

    # 좋아하는 영화배우
    liked_actors = models.ManyToManyField(Actor, related_name='like_actors_users', blank=True)
    # 좋아하는 감독
    liked_directors = models.ManyToManyField(Director, related_name='like_directors_users', blank=True)
