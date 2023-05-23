from rest_framework import serializers

from .models import Actor, Director, Genre, Movie, WorldCupItem


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'popularity', 'vote_average',
                  'overview', 'poster_path', 'backdrop_path', 'genre_ids']


class RandomMovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = WorldCupItem
        fields = ['id', 'title', 'poster_path', 'genre_ids']
