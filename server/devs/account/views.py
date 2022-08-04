from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny

from django.http import Http404

from .serializers import UserSerializer, UserLoginSerializer
from .models import User

# from django.shortcuts import redirect, get_object_or_404
# from django.contrib.auth import get_user_model

# Create your views here.


class Test(APIView):
    def get(self, req):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, req):
        serializer = UserSerializer(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # serializer 내부의 create() 호출
        status_code = status.HTTP_201_CREATED  # 성공
        response = {
            'success': "true",
            'status code': status_code,
            'message': "user registered successfully",
        }
        return Response(response, status=status_code)


class UserLoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            "success": "True",
            "status_code": status.HTTP_200_OK,
            "message": "User Logged in successfully",
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


# def follow(request, pk):
#     User = get_user_model()
#     # 팔로우 당하는 사람
#     user = get_object_or_404(User, pk=pk)
#     if user != request.user:
#         # 팔로우를 요청한 사람 => request.user
#         # 팔로우가 되어 있다면,
#         if user.followers.filter(pk=request.user.pk).exists():
#             # 삭제
#             user.followers.remove(request.user)
#         else:
#             # 추가
#             user.followers.add(request.user)
#     return redirect('accounts:detail', user.pk)
