from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField(max_length=4)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    ranking = models.IntegerField(max_length=10)

    def __str__(self):
        return "{}".format(self.user.username, self.age)
