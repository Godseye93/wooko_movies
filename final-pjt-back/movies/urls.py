from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_search, name='search'),  # 영화 검색
    path('recommended/', views.movie_sort),
    path('<int:movie_pk>/', views.movie_detail),  # 단일 영화 조회

    # 장르기반 영화 추천
    path('random/', views.get_random_movies, name='get_random_movies'),  # 랜덤영화 추첨
    path('random-by-genre/', views.get_random_movie_by_genre, name='get_random_movie_by_genre'),  # 장르기반 영화추첨
    path('get_liked_genres/', views.get_liked_genres, name='get_liked_genres'),  # 좋아하는 장르 추가

    # 배우기반 영화 추천
    path('random_actor/', views.get_random_actors, name='get_random_actors'),  # 랜덤배우 추첨
    path('random-by-actor/', views.get_random_movie_by_actor, name='get_random_movie_by_actor'),  # 배우기반 영화추첨
    path('get_liked_actor/', views.get_liked_actors, name='get_liked_actors'),  # 좋아하는 배우 추가

    # 감독기반 영화 추천
    path('random_director/', views.get_random_directors, name='get_random_directors'),  # 랜덤감독 추첨
    path('random-by-director/', views.get_random_movie_by_director, name='get_random_movie_by_director'),  # 감독기반 영화추첨
    path('get_liked_director/', views.get_liked_directors, name='get_liked_directors'),  # 좋아하는 감독 추가
]

# path('VS/', views.get_random_VS_movies, name='get_random_VS_movies')
# 메인 페이지 추천영화 목록 (평점순, 최신순, 개봉예정순)
# path('movies', views.movies_main),  # 모든 영화 목록 조회
# path('<int:movie_pk>/rate/<int:rate_pk>/',
#      views.movie_rate_update_or_delete),  # 로그인 유저의 평점 수정/삭제
# path('<int:user_pk>/rate_list/', views.movie_rate_list),  # 평점 조회
# path('<int:movie_pk>/rate/', views.movie_rate),  # 로그인 유저의 평점 등록
# path('create/', views.movie_create),  # 영화 등록
