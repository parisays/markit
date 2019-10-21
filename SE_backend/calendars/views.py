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

    def get_queryset(self):
        calendar_id = self.kwargs['calendar_id']
        calendar = generics.get_object_or_404(Calendar, id=calendar_id)

        return Calendar.objects.filter(calendar=calendar)

    def list(self, request):
        user = self.request.user
        return Calendar.objects.filter(user=user)

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

    serializer_class = PostSerializer

    def list(self, request):
        user = self.request.user
        return Post.objects.filter(user=user)


class PostView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = PostSerializer
    queryset = Post.objects.all()

