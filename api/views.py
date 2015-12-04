from api.seriallzers import ChallengevSeriallzer, LikeSeriallzer
from django.shortcuts import render
from rest_framework import generics, permissions, filters
from challenge.models import *


class APIListCreateChallengev(generics.ListCreateAPIView):
    queryset = Challengev.objects.order_by('-post_at')
    serializer_class = ChallengevSeriallzer

    def perform_create(self, serializer):
        serializer.save()


class APIDetailUpdateChallengev(generics.RetrieveUpdateDestroyAPIView):
    queryset = Challengev.objects.order_by('-post_at')
    serializer_class = ChallengevSeriallzer


class APIListCreateLike(generics.ListCreateAPIView):
    queryset = Like.objects.order_by('-post_at')
    serializer_class = LikeSeriallzer

    def perform_create(self, serializer):
        serializer.save()


class APIDetailUpdateLike(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.order_by('-post_at')
    serializer_class = LikeSeriallzer

