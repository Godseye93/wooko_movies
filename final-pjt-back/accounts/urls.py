from django.urls import path

from . import views

app_name = 'accounts'

# 토큰으로 삭제된 usl
# path('signup/', views.user_signup, name='signup'),   # 회원가입
# path('login/', views.user_login, name='user_login'),  # 로그인
# path('logout/', views.user_logout, name='user_logout'),  # 로그아웃

urlpatterns = [
    path('', views.user_delete, name='user_delete'),  # 회원탈퇴
    path('<int:user_pk>/profile/', views.user_profile, name='user_profile'),  # 상대방 프로필 조회
    path('profile/', views.user_profile, name='user_profile'),  # 프로필 수정
    path('<int:user_pk>/follow/', views.follow),  # 팔로우 등록 및 해제 + 팔로우 수까지 포함
    path('<int:user_pk>/follow/list/', views.follow_list),  # 팔로우 조회
]
