from django.contrib.auth.models import User
from rest_framework import serializers
from challenge.models import *


class ChallengevSeriallzer(serializers.ModelSerializer):
    class Meta:
        model = Challengev
        fields = ('id','title', 'description', 'user', 'video', 'post_at', 'subs', 'likes')


class SubmissionvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submissionv
        fields = ('challenge', 'likes', 'title', 'user', 'video', 'post_at', 'mod_at')



class LikeSeriallzer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('like', 'post_at', 'mod_at')






