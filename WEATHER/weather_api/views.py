from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import TODOLIST
from .serializers import TODOSerializer

class ListTodo(generics.ListCreateAPIView):
    queryset = TODOLIST.objects.all()
    serializer_class = TODOSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = TODOLIST.objects.all()
    serializer_class = TODOSerializer
