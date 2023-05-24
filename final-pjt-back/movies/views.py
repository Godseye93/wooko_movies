import random

from accounts.models import UserLikedActors, UserLikedDirectors
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import (api_view, permission_classes,
                                       renderer_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Actor, Director, Movie
from .serializers import (MovieActorSerializer, MovieDirectorSerializer,
                          MovieSerializer, RandomActorSerializer,
                          RandomDirectorSerializer, RandomMovieSerializer)


# 분류된 영화 목록 조회
@api_view(['GET'])
def movie_sort(request):
    sort_by = request.GET.get('sort_by')  # 정렬 기준 파라미터 받기
    movies = Movie.objects.all()

    # if sort_by == 'popularity':
    #     movies = movies.order_by('-popularity')
    if sort_by == 'vote_average':
        movies = movies.order_by('-vote_average')
    elif sort_by == 'release_date':
        movies = movies.order_by('-release_date')

    serializer = MovieSerializer(movies[:8], many=True)  # 상위8개
    return Response(serializer.data)
    # url 사용법
    # movies/recommended/?sort_by=popularity
    # movies/recommended/?sort_by=vote_average
    # movies/recommended/?sort_by=release_date


# 영화 상세 정보 조회
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 영화 검색 기능
@api_view(['GET'])
def movie_search(request):
    search = request.GET.get('search', '')
    movies = Movie.objects.filter(title__icontains=search)
    serializer = MovieSerializer(movies, many=True)
    data = {'movies': serializer.data, 'search': search}
    return Response(data)


# 랜덤영화 추첨
@api_view(['GET'])
def get_random_movies(request):
    count = request.GET.get('count', 16)  # 요청 매개변수 'count'를 가져오고, 기본값은 16으로 설정
    movies = list(Movie.objects.all())
    random_movies = random.sample(movies, int(count))
    serializer = RandomMovieSerializer(random_movies, many=True)
    return Response(serializer.data)


# 추천 영화로 '좋아하는 장르' 추가
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_liked_genres(request):
    movies = request.data
    user = request.user

    for movie in movies:
        movie_id = movie.get('id')
        try:
            movie_obj = Movie.objects.get(id=movie_id)  # id에 해당하는 영화를 가져옵니다
            user.liked_genres.add(*movie_obj.genre_ids.all())
        except Movie.DoesNotExist:
            return Response("영화가 없음", status=status.HTTP_404_NOT_FOUND)

    return Response("장르가 성공적으로 추가")


# 장르기반 영화추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_random_movie_by_genre(request):
    user = request.user
    liked_genres = user.liked_genres.all()

    # 사용자가 좋아하는 장르가 있는 경우
    if liked_genres:
        random_movies = []
        for _ in range(8):
            genre = random.choice(liked_genres)  # 좋아하는 장르 중에서 랜덤하게 하나를 선택
            movies = Movie.objects.filter(genre_ids__id=genre.id)  # 해당 장르를 가지는 영화들을 필터링

            if movies:
                random_movie = random.choice(movies)  # 해당 장르의 영화 중에서 랜덤하게 하나를 선택
                random_movies.append(random_movie)

        serializer = MovieSerializer(random_movies, many=True)
        return Response(serializer.data)
    else:
        Response("좋아하는 장르가 없습니다.")

    return Response("검색 결과가 없습니다.")


# 랜덤배우 추첨
@api_view(['GET'])
def get_random_actors(request):
    count = request.GET.get('count', 16)  # 요청 매개변수 'count'를 가져오고, 기본값은 16으로 설정
    actors = list(Actor.objects.all())
    random_actors = random.sample(actors, int(count))
    serializer = RandomActorSerializer(random_actors, many=True)
    return Response(serializer.data)


# 추천 영화로 '좋아하는 배우' 추가
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_liked_actors(request):
    actors = request.data
    user = request.user

    for actor in actors:
        actor_name = actor.get('name')
        try:
            actor_obj = Actor.objects.get(name=actor_name)
            liked_actor = UserLikedActors.objects.create(user=user, actor=actor_obj, name=actor_name)
            user.liked_actors.add(liked_actor)
        except Actor.DoesNotExist:
            return Response("배우가 없음", status=status.HTTP_404_NOT_FOUND)

    return Response("배우가 성공적으로 추가")


# 배우기반 영화추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_random_movie_by_actor(request):
    user = request.user
    liked_actors = user.liked_actors.all()

    # 사용자가 좋아하는 배우가 있는 경우
    if liked_actors:
        movies = []
        random_actors = random.sample(list(liked_actors), k=min(len(liked_actors), 8))
        for actor in random_actors:
            actor_movies = Actor.objects.filter(name=actor.name)
            for movie in actor_movies:
                movie_data = {
                    'title': movie.title,
                    'release_date': movie.release_date,
                    'popularity': movie.popularity,
                    'vote_average': movie.vote_average,
                    'overview': movie.overview,
                    'poster_path': movie.poster_path,
                    'genre_ids': movie.genre_ids,
                    'backdrop_path': movie.backdrop_path,
                }
                movies.append(movie_data)

        serializer = MovieActorSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        return Response("좋아하는 배우가 없습니다.")


# 랜덤감독 추첨
@api_view(['GET'])
def get_random_directors(request):
    count = request.GET.get('count', 16)  # 요청 매개변수 'count'를 가져오고, 기본값은 16으로 설정
    directors = list(Director.objects.all())
    random_directors = random.sample(directors, int(count))
    serializer = RandomDirectorSerializer(random_directors, many=True)
    return Response(serializer.data)


# 추천 영화로 '좋아하는 감독' 추가
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_liked_directors(request):
    directors = request.data
    user = request.user

    for director in directors:
        director_name = director.get('name')
        try:
            director_obj = Director.objects.get(name=director_name)
            liked_director = UserLikedDirectors.objects.create(user=user, director=director_obj, name=director_name)
            user.liked_directors.add(liked_director)
        except Director.DoesNotExist:
            return Response("감독이 없음", status=status.HTTP_404_NOT_FOUND)

    return Response("감독이 성공적으로 추가")


# 감독기반 영화추천
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_random_movie_by_director(request):
    user = request.user
    liked_directors = user.liked_directors.all()

    # 사용자가 좋아하는 감독이 있는 경우
    if liked_directors:
        movies = []
        random_directors = random.sample(list(liked_directors), k=min(len(liked_directors), 8))
        for director in random_directors:
            director_movies = Director.objects.filter(name=director.name)
            for movie in director_movies:
                movie_data = {
                    'title': movie.title,
                    'release_date': movie.release_date,
                    'popularity': movie.popularity,
                    'vote_average': movie.vote_average,
                    'overview': movie.overview,
                    'poster_path': movie.poster_path,
                    'genre_ids': movie.genre_ids,
                    'backdrop_path': movie.backdrop_path,
                }
                movies.append(movie_data)

        serializer = MovieDirectorSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        return Response("좋아하는 감독이 없습니다.")


# def get_random_VS_movies():
#     movies = list(Movie.objects.all())  # 모든 영화 정보를 가져옵니다.
#     random_movies = random.sample(movies, 8)  # 영화 정보에서 랜덤하게 16개를 선택합니다.
#     serializer = RandomMovieSerializer(random_movies, many=True)  # 시리얼라이저를 사용하여 데이터를 직렬화합니다.
#     return Response(serializer.data)

# def movie_search(request):
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)


# # 메인 영화 목록을 반환
# @api_view(['GET'])
# def movies_main(request):
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)

# # 영화 등록 (잘되는지는 모름)
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def movie_create(request):
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

# # 영화 평점 등록
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def movie_rate(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = RateSerializer(data=request.data)
#     if serializer.is_valid():
#         rate = serializer.save(movie=movie, user=request.user)
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)


# # 사용자의 영화 평점 목록
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def movie_rate_list(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     rates = user.user_rated_movie.all()
#     serializer = RateSerializer(rates, many=True)
#     return Response(serializer.data)


# # 로그인 유저의 평점 수정/삭제
# @api_view(['PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def movie_rate_update_or_delete(request, movie_pk, rate_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     rate = get_object_or_404(Rate, pk=rate_pk, movie=movie, user=request.user)
#     if request.method == 'PUT':
#         serializer = RateSerializer(rate, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         rate.delete()
#         return JsonResponse({'message': 'Rate deleted successfully'}, status=204)
