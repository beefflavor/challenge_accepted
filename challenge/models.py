from django.db import models


# class Profile(models.Model):
#     username = models.CharField(max_length=20)


class Challenge(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(Profile)


class Like(models.Model):
    user = models.ForeignKey(User)
