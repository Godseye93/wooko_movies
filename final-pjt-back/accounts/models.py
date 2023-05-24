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


class UserLikedDirectors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_directors')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='liked_by_users')
    name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'accounts_user_liked_directors'


class UserLikedActors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_actors')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='liked_by_users')
    name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'accounts_user_liked_actors'



