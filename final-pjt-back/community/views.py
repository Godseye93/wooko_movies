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
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


# 단일 게시글 조회, 수정, 삭제
@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail_or_update_or_delete(request, article_pk):
    # 단일 게시글 조회(임시 나중에 고쳐야함)
    def article_detail(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 게시글 수정하기
    def article_update(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # 게시글 삭제하기
    def article_delete(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return Response(status=204)

    if request.method == 'GET':
        return article_detail(request, article_pk)
    elif request.method == 'PUT':
        return article_update(request, article_pk)
    elif request.method == 'DELETE':
        return article_delete(request, article_pk)


# 게시글 작성하기
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# 댓글 수정, 삭제
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_or_delete(request, article_pk, comment_pk):

    # 댓글 수정하기
    @api_view(['PUT'])
    @permission_classes([IsAuthenticated])
    def comment_update(request, article_pk, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk, article_pk=article_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # 댓글 삭제하기
    @api_view(['DELETE'])
    @permission_classes([IsAuthenticated])
    def comment_delete(request, article_pk, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk, article_pk=article_pk)
        comment.delete()
        return Response(status=204)

    if request.method == 'PUT':
        return comment_update(request, article_pk, comment_pk)
    elif request.method == 'DELETE':
        return comment_delete(request, article_pk, comment_pk)


# 댓글 작성하기
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    request.data['article'] = article_pk
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


#  게시글 좋아요 등록 및 해제
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)

    serializer = ArticleSerializer(article)

    like_status = {
        'id': serializer.data.get('id'),
        'like_count': article.like_users.count(),
        'like_users': serializer.data.get('like_users'),
    }
    return Response(like_status)
