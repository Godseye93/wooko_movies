from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer


# 모든 게시글 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def article_list(request):
    articles = get_object_or_404(Article)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


# 단일 게시글 조회(임시 나중에 고쳐야함)
@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


# 게시글 작성하기
@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# 게시글 수정하기
@api_view(['PUT'])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# 게시글 삭제하기
@api_view(['DELETE'])
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return Response(status=204)


# 댓글 작성하기
@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, article=article)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# 댓글 수정하기
@api_view(['PUT'])
def comment_update(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, article__pk=article_pk)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# 댓글 삭제하기
@api_view(['DELETE'])
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, article__pk=article_pk)
    comment.delete()
    return Response(status=204)
