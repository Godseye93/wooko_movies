from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import *
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

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


# 상대방 프로필 조회
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request, user_pk=None):
    user = User.objects.get(pk=user_pk) if user_pk else request.user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
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