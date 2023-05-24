from django.conf import settings
from django.db import models


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)  # 장르 id
    name = models.CharField(max_length=50)  # 장르 name


class Movie(models.Model):
    title = models.CharField(max_length=100)  # 제목
    release_date = models.DateField(null=True, blank=True)  # 개봉일
    popularity = models.FloatField(null=True, blank=True)  # 관객 수
    vote_average = models.FloatField(null=True, blank=True)  # 평점
    overview = models.TextField(null=True, blank=True)  # 줄거리
    poster_path = models.CharField(
        max_length=200, null=True, blank=True)  # 이미지
    genre_ids = models.ManyToManyField(Genre)
    backdrop_path = models.CharField(max_length=200, null=True, blank=True)


class WorldCupItem(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    poster_path = models.CharField(
        max_length=200, null=True, blank=True)  # 이미지
    genre_ids = models.CharField(max_length=100)


class ActorWorldCupItem(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(
        max_length=200, null=True, blank=True)  # 이미지


class DirectorWorldCupItem(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(
        max_length=200, null=True, blank=True)  # 이미지


class Director(models.Model):
    model = models.CharField(max_length=20)
    name = models.CharField(max_length=255, null=True)
    profile_path = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=255, null=True)
    genre_ids = models.ManyToManyField(Genre)
    backdrop_path = models.CharField(max_length=255, null=True)


class Actor(models.Model):
    model = models.CharField(max_length=20)
    name = models.CharField(max_length=255, null=True)
    profile_path = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=255, null=True)
    genre_ids = models.ManyToManyField(Genre)
    backdrop_path = models.CharField(max_length=255, null=True)
