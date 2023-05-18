from django.urls import path

from . import views

app_name = 'movies'

urlpatterns = [
    path('movies/', views.movie_list),  # 모든 영화 목록 조회
    path('movies/recommend/', views.movie_sort),
    path('movie/<int:movie_pk>/', views.movie_detail),  # 단일 영화 조회
]

# 메인 페이지 추천영화 목록 (평점순, 최신순, 개봉예정순)
# path('movies', views.movies_main),  # 모든 영화 목록 조회
# path('<int:movie_pk>/rate/<int:rate_pk>/',
#      views.movie_rate_update_or_delete),  # 로그인 유저의 평점 수정/삭제
# path('<int:user_pk>/rate_list/', views.movie_rate_list),  # 평점 조회
# path('<int:movie_pk>/rate/', views.movie_rate),  # 로그인 유저의 평점 등록
# path('create/', views.movie_create),  # 영화 등록