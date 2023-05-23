from rest_framework import serializers

from .models import (ActorWorldCupItem, DirectorWorldCupItem, Genre, Movie,
                     WorldCupItem)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'popularity', 'vote_average',
                  'overview', 'poster_path', 'backdrop_path', 'genre_ids']


class RandomActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorWorldCupItem
        fields = ['id', 'title', 'poster_path', 'genre_ids']


class RandomDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorWorldCupItem
        fields = ['id', 'name', 'profile_path']


class RandomMovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = WorldCupItem
        fields = ['id', 'name', 'profile_path']
