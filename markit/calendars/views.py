from django.shortcuts import render
from calendars.models import *
from calendars.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class CalendarListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

    def list(self, request):
        user = self.request.user
        # print(user)
        calendar_list = Calendar.objects.filter(user=user)
        serializer = self.get_serializer(calendar_list, many=True)
        return Response(serializer.data)

class CalendarView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = CalendarSerializer
    queryset = Calendar.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PostListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        calendar_id = self.request.query_params.get('calendar_id')
        # print("calendar id is : " , calendar_id)
        calendar = Calendar.objects.get(id=calendar_id)
        post_list = Post.objects.filter(calendar=calendar)
        serializer = self.get_serializer(post_list, many=True)
        return Response(serializer.data)


class PostView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = PostSerializer
    queryset = Post.objects.all()

