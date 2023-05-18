from django.urls import path

from . import views

app_name = 'accounts'


urlpatterns = [
    # rest_auth 때문에 여기서 처리 안하고 finalbaek에 가면 처리되어있음
    # path('signup/', views.user_signup, name='signup'),   # 회원가입
    path('', views.user_delete, name='user_delete'),  # 회원탈퇴
    path('login/', views.user_login, name='user_login'),  # 로그인
    path('logout/', views.user_logout, name='user_logout'),  # 로그아웃
    path('<int:user_pk>/profile/', views.user_profile, name='user_profile'),  # 상대방 프로필 조회
    path('profile/', views.user_profile, name='user_profile'),  # 프로필 수정
]
