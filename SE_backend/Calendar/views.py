from django.shortcuts import render
from Calendar.models import *
from Calendar.serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CalendarListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer


class CalendarView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()


class PostListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = PostSerializer
    queryset = Post.objects.all()