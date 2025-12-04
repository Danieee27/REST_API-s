from rest_framework import serializers
from .models import UserAccount, OTP, Conversation, Message
from django.contrib.auth.models import User

class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ["id", "Firstname", "Lastname", "Phone", "date_joined"]

    def create(self, validated_data):
        user = UserAccount.objects.create_user(
            Firstname = validated_data['Firstname'],
            Lastname = validated_data['Lastname'],
            Phone = validated_data['Phone']
        )
        user.save()
        return user

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ["Phone", "OTP"]

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ["id", "sender", "receiver", "created_at"]

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        pass