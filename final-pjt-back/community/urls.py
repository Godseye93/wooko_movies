from django.urls import path

from . import views

app_name = 'community'
urlpatterns = [
    # # review
    path('all/', views.article_list),  # 모든 게시글 목록 조회

    # 단일 게시글 조회 or 게시글 수정하기 or 게시글 삭제하기
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('', views.article_create),  # 게시글 작성하기

    # path('<int:article_pk>/', views.article_update_or),  # 게시글 수정하기
    # path('<int:article_pk>/', views.article_delete),  # 게시글 삭제하기

    path('<int:article_pk>/comment/', views.comment_create),

    path('<int:article_pk>/comment/<int:comment_pk>/', views.comment_update_or_delete),  # 댓글 작성하기
    # path('<int:article_pk>/comment/', views.comment_update),  # 댓글 수정하기
    # path('<int:article_pk>/comment/', views.comment_delete),  # 댓글 삭제하기

    path('<int:review_pk>/like/', views.article_like),  # 게시글 좋아요 / 좋아요 취소
]
