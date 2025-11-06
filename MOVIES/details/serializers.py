from rest_framework import serializers
from .models import Detail
import requests

class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detail
        fields = ['id', 'title', 'description', 'realease_year', 'streaming_platform', 'rating']


   
        


