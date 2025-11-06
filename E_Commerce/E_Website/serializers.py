from rest_framework import serializers
from .models import Product, Profile, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "description", "size_range"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "Username", "Phone", "Email_Address", "Address"]
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["Product", "Preferred_size"]