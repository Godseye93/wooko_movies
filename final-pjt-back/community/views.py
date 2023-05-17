# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404, render

# from .models import Article, Comment

# # 모든 게시글 목록 조회
# def article_list(request):
#     articles = Article.objects.all()
#     data = {
#         'articles': [
#             {
#                 'id': article.id,
#                 'title': article.title,
#                 'content': article.content,
#             }
#             for article in articles
#         ]
#     }
#     return JsonResponse(data)

# # 단일 게시글 조회


# def article_detail(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     data = {
#         'id': article.id,
#         'title': article.title,
#         'content': article.content,
#     }
#     return JsonResponse(data)

# # 게시글 작성하기


# def article_create(request):
#     return JsonResponse({})

# # 게시글 수정하기


# def article_update(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     return JsonResponse({})

# # 게시글 삭제하기


# def article_delete(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     return JsonResponse({})

# # 댓글 작성하기


# def comment_create(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     return JsonResponse({})

# # 댓글 수정하기


# def comment_update(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     return JsonResponse({})

# # 댓글 삭제하기


# def comment_delete(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     return JsonResponse({})
