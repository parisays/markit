from django.shortcuts import render
from Calendar.models import *
from Calendar.serializers import *
from rest_framework import generics

# Create your views here.

class CalendarListView(generics.ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer


class CalendarView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()