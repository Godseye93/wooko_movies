from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer


# 분류된 영화 목록 조회
@api_view(['GET'])
def movie_sort(request):
    sort_by = request.GET.get('sort_by')  # 정렬 기준 파라미터 받기
    movies = Movie.objects.all()

    if sort_by == 'popularity':
        movies = movies.order_by('-popularity')
    elif sort_by == 'vote_average':
        movies = movies.order_by('-vote_average')
    elif sort_by == 'release_date':
        movies = movies.order_by('release_date')

    serializer = MovieSerializer(movies[:8], many=True)  # 상위8개만뽑는데 내림차순인지 오름차순인지 모름 진짜 모름
    return Response(serializer.data)
    # url 사용법
    # movies/recommend/?sort_by=popularity
    # movies/recommend/?sort_by=vote_average
    # movies/recommend/?sort_by=release_date


# 영화 상세 정보 조회
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

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
