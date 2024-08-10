from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginAPIView(APIView):
    def post(self, request):
        user = authenticate(
            studentNumber=request.data['studentNumber'],
            password=request.data['password']
        )
        if user is not None:
            serializer = UserSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "User logged in successfully.",
                    "token": {
                        "refresh": refresh_token,
                        "access": access_token
                    },
                },
                status=status.HTTP_200_OK
            )
            res.set_cookie("access_token", access_token, httponly=True) #httponly js로부터 방어
            res.set_cookie("refresh_token", refresh_token, httponly=True)
            return res
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
            

class LogoutAPIView(APIView):
    def post(self, request):
        res = Response({"message": "User logged out successfully."}, status=status.HTTP_200_OK)
        res.delete_cookie("access_token")
        res.delete_cookie("refresh_token")
        return res