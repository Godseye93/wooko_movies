from django.urls import path

from . import views

app_name = 'accounts'


urlpatterns = [
    # path('user/signup/', views.user_signup),   # 회원가입
    # path('user', views.user_delete,),  # 회원탈퇴
    # path('user/login/', views.user_login),  # 로그인
    # path('user/logout/', views.user_out),  # 로그아웃
    # path('user/<int:user_pk>/profile/', views.user_profile),  # 상대방 프로필 조회
    # path('user/profile/', views.user_profile),  # 프로필 수정
]
