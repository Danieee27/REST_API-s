from django.shortcuts import render

# Create your views here.
#viewsets define what is shown in the api and how it behaves
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import redirect, get_object_or_404
from .models import URL
from .serializers import URLSerializer

class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    lookup_field = 'short_code'

    #Custom action for redirection
    @action(detail = True, methods = ['get'])
    def redirect_to_long_url(self, request, short_code = None):
        url_instance = get_object_or_404(URL, short_code=short_code)
        url_instance.clicks += 1
        url_instance.save()
        return redirect(url_instance.long_url)