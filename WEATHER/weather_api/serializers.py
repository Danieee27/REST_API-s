from rest_framework import serializers
from .models import TODOLIST


class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODOLIST
        fields = ["id", "Work", "Time", "status"]


        
            