from rest_framework import serializers

from .models import Actor, Director, Genre, Movie, WorldCupItem


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


class MovieDirectorSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'popularity', 'vote_average',
                  'overview', 'poster_path', 'backdrop_path', 'genre_ids']


class MovieActorSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'popularity', 'vote_average',
                  'overview', 'poster_path', 'backdrop_path', 'genre_ids']


class RandomActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'poster_path']


class RandomDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'profile_path']


class RandomMovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = WorldCupItem
        fields = ['id', 'title', 'poster_path', 'genre_ids']
