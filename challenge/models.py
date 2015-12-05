from django.contrib.auth.models import User
from django.db import models


# class Profile(models.Model):
#     username = models.CharField(max_length=20)


class Challengev(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User)
    video = models.URLField(max_length=255)
    post_at = models.DateTimeField(auto_now_add=True)

    @property
    def likes(self):
        like_count = self.like_set.count()
        return like_count

    @property
    def subs(self):
        all_subs = self.submissionv_set.count()
        return all_subs

    def __str__(self):
        return "{}".format(self.title,)


class Submissionv(models.Model):
    user = models.ForeignKey(User)
    challenge = models.ForeignKey(Challengev)
    title = models.CharField(max_length=255)
    video = models.URLField(max_length=255)
    post_at = models.DateTimeField(auto_now_add=True)
    mod_at = models.DateTimeField(auto_now=True)

    @property
    def likes(self):
        like_count = self.submissionlike_set.count()
        return like_count


class Like(models.Model):
    like = models.ForeignKey(Challengev)
    user = models.ForeignKey(User)
    post_at = models.DateTimeField(auto_now_add=True)
    mod_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.user,)

class SubmissionLike(models.Model):
    like = models.ForeignKey(Submissionv)
    user = models.ForeignKey(User)
    post_at = models.DateTimeField(auto_now_add=True)
    mod_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.user,)


# class Challengep(models.Model):
#     title = models.CharField(max_length=20)
#     description = models.CharField(max_length=200)
#     user = models.ForeignKey(User)
#     picture = models.ImageField(upload_to='challenge_pictures')
#     post_at = models.DateTimeField(auto_now_add=True)
#     mod_at = models.DateTimeField(auto_now=True)
