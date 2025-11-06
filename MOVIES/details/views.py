from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Detail
import requests
from .serializers import DetailSerializer
from rest_framework.response import Response

api_key = '8180967780f089640ddc5bef8196dc28'

class DetailView(APIView):

    def get(self, request):
        name = request.query_params.get('movie_name')

        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={name}'
        data = requests.get(url).json()
        if name:
            return Response(data)
