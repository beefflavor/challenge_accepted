from django.contrib.auth.models import User
from rest_framework import serializers
from challenge.models import *
from users.models import *


class ChallengevSeriallzer(serializers.ModelSerializer):
    class Meta:
        model = Challengev
        fields = ('id', 'title', 'description', 'user', 'video', 'post_at', 'subs', 'likes')


class SubmissionvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submissionv
        fields = ('id', 'challenge', 'likes', 'title', 'user', 'video', 'post_at', 'mod_at')


class LikeSeriallzer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'like', 'post_at', 'mod_at')


class ProfileSeriallzer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'age', 'profile_picture')
