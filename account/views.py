from django.shortcuts import render

# Create your views here.
import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.core.mail import EmailMessage
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import AuthenticationFailed
import base64

from .models import Account, RegisterCodeBuffer
from todo.models import Todo
from .serializers import RegisterSerializer, LoginSerializer
from .security import create_email_code

import base64


#가입
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "account": serializer.data,
                    "resultCode": 200,
                    },
                status=status.HTTP_200_OK,
            )
        return Response({"resultCode":500, "account":None}, status=status.HTTP_400_BAD_REQUEST)


#로그인
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        result = serializer.validated_data
        
        if "Login Error" == result:
            return Response({"resultCode":500, "token":None, "nickname":None, "email":None, "image":None}, status=status.HTTP_200_OK)
        
        login_data = result
        return Response(dict({"resultCode":200}, **login_data), status=status.HTTP_200_OK)
    
