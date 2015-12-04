from django.contrib.auth.models import User
from django.db import models


# class Profile(models.Model):
#     username = models.CharField(max_length=20)


class Challengev(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    video = models.URLField(max_length=255)
    post_at = models.DateTimeField(auto_now_add=True)
    mod_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    like = models.ForeignKey(Challengev)
    post_at = models.DateTimeField(auto_now_add=True)
    mod_at = models.DateTimeField(auto_now=True)


# class Challengep(models.Model):
#     title = models.CharField(max_length=20)
#     description = models.CharField(max_length=200)
#     user = models.ForeignKey(User)
#     picture = models.ImageField(upload_to='challenge_pictures')
