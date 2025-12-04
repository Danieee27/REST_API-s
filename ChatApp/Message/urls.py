from django.urls import path
from .views import AccountList, OTPList, VERIFYOTPView, SENDOTPView

urlpatterns = [
    path('accounts/', AccountList.as_view()),
    path('verify_otp/', VERIFYOTPView.as_view()),
    path('send_otp/', SENDOTPView.as_view()),
    ]