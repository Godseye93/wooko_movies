from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import *
from rest_framework.response import Response

from .models import User
from .serializers import FollowSerializer, UserSerializer

# # 회원가입
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def user_signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 회원탈퇴
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def user_delete(request):
    request.user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# # 로그인
# @api_view(['POST'])
# def user_login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     if username and password:
#         user = User.objects.filter(username=username).first()
#         if user and user.check_password(password):
#             # 로그인 성공
#             return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
#     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# # 로그아웃
# @api_view(['POST'])
# def user_logout(request):
#     return Response(status=status.HTTP_200_OK)


# 프로필 조회 / 수정
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request, user_pk=None):
    user = User.objects.get(pk=user_pk) if user_pk else request.user

    if request.method == 'GET':
        serializer = UserSerializer(user)
        response_data = serializer.data

        # 팔로우 관련 정보 추가
        # response_data['followers_count'] = user.followings.count()
        # response_data['followers_list'] = user.followings.count()
        # response_data['followings_list'] = user.followings.count()

        return Response(response_data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 프로필 수정
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 팔로우 등록 및 해제
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # 인증된 사용자만 권한 허용
def follow(request, user_pk):
    # user_pk : 팔로우 하려는 사람의 pk
    follow_user = get_object_or_404(User, pk=user_pk)
    # 나
    user = request.user
    # 나 와 팔로우 하려는 사람이 다를때
    if follow_user != user:
        # 기존의 팔로우 목록에 추가하려는 사람이 있다면 지우고 / 아니면 추가
        if follow_user.followings.filter(pk=user.pk).exists():
            follow_user.followings.remove(user)
        else:
            follow_user.followings.add(user)

        serializer = FollowSerializer(follow_user)

        follow_status = {
            # 그 사람을 팔로우 한 사람의 숫자
            'follower_count': follow_user.followings.count(),
            # 그 사람을 팔로우 한 사람의 목록
            'follow_list': serializer.data.get('followings'),
            # 내가(혹은 해당 pk가) 팔로우 한 사람의 수
            'following_count': follow_user.followers.count(),
        }
    return Response(follow_status)


# # 팔로우 조회
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def follow_list(request, user_pk):
#     follow_user = get_object_or_404(User, pk=user_pk)
#     serializer = FollowSerializer(follow_user)

#     follow_status = {
#         # 그 사람을 팔로우 한 사람의 숫자
#         'follower_count': follow_user.followings.count(),
#         # 그 사람을 팔로우 한 사람의 목록
#         'follow_list': serializer.data.get('followings'),
#         # 내가(혹은 해당 pk가) 팔로우 한 사람의 수
#         'following_count': follow_user.followers.count(),
#     }
#     return Response(follow_status)
