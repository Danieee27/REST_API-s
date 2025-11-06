from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product, Profile, Order
from .serializers import ProductSerializer, UserSerializer, OrderSerializer

class ListProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListUsers(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

class ListOrders(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

