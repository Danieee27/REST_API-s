import os
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserAccount, OTP
from .serializers import UserAccountSerializer, OTPSerializer
from rest_framework.response import Response
from termii.token import Token
from termii.schemas.token import TokenType
from django.conf import settings
from dotenv import load_dotenv

# Create your views here.
load_dotenv()



token_client = Token()
token_client.authenticate_from_env()   


class AccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

class OTPList(generics.ListAPIView):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer

class SENDOTPView(APIView):
    def post(self, request):
        phone = request.data.get("Phone")
        if phone:
            response = token_client.send_token( #function to send code
                message_type=TokenType.NUMERIC, 
                receiver=phone,
                pin_length=6,           # 6-digit OTP
                pin_time_to_live=5      # minutes OTP is valid
            )
            return Response({"message": "OTP sent successfully", "data": response})

        OTP.update_or_create(Phone = phone)

class VERIFYOTPView(APIView):
    def post(self, request):
        phone = request.data.get("Phone")
        otp = request.data.get("OTP")

        
        if otp:
            response = token_client.verify_token(
                receiver=phone,
                token=otp
            )
            if response.get('valid'):
                user = UserAccount.objects.get(Phone=phone)
                refresh = RefreshToken.for_user(user)
                return Response(
                    {"message": "OTP is valid",
                "access": str(refresh.access_token),
                "refresh": str(refresh)})

        else:
            return Response({"message": "OTP is invalid or expired"})