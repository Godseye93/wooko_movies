from django.conf import settings
from django.db import models


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)  # 장르 id
    name = models.CharField(max_length=50)  # 장르 name


class Actor(models.Model):
    id = models.IntegerField(primary_key=True)  # 배우 id
    name = models.CharField(max_length=50)  # 배우 name


class Director(models.Model):
    id = models.IntegerField(primary_key=True)  # 감독 id
    name = models.CharField(max_length=50)  # 감독 name


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
    title = models.CharField(max_length=100)
    poster_path = models.CharField(
        max_length=200, null=True, blank=True)  # 이미지
    genre_ids = models.CharField(max_length=100)


class WorldCupItemActor(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(
        max_length=200, null=True, blank=True)  # 이미지


class WorldCupItemDirector(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(
        max_length=200, null=True, blank=True)  # 이미지
