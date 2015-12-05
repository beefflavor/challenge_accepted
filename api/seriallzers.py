from django.contrib.auth.models import User
from rest_framework import serializers
from challenge.models import *


class ChallengevSeriallzer(serializers.ModelSerializer):
    class Meta:
        model = Challengev
        fields = ('title', 'description', 'user', 'video', 'post_at', 'subs')


class SubmissionvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submissionv
        fields = ('challenge', 'title', 'user', 'video', 'post_at', 'mod_at')



class LikeSeriallzer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('like', 'post_at', 'mod_at')






