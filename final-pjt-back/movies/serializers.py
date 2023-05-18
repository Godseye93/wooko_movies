from rest_framework import serializers

from .models import Genre, Movie


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
