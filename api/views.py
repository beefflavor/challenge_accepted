from api.seriallzers import *
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



class APIListCreateSubmissionv(generics.ListCreateAPIView):
    queryset = Submissionv.objects.order_by('-post_at')
    serializer_class = SubmissionvSerializer

    def perform_create(self, serializer):
        serializer.save()


class APIDetailUpdateSubmissionv(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submissionv.objects.order_by('-post_at')
    serializer_class = SubmissionvSerializer


class APIListCreateLike(generics.ListCreateAPIView):
    queryset = Like.objects.order_by('-post_at')
    serializer_class = LikeSeriallzer

    def perform_create(self, serializer):
        serializer.save()


class APIDetailUpdateLike(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.order_by('-post_at')
    serializer_class = LikeSeriallzer

