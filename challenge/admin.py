from django.contrib import admin
from challenge.models import *


@admin.register(Challengev)
class ChallengevAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'video', 'post_at')


@admin.register(Submissionv)
class SubmissionvAdmin(admin.ModelAdmin):
    list_display = ('challenge', 'title', 'user', 'video', 'post_at', 'mod_at')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('like', 'post_at', 'mod_at')


# @admin.register(Challengep)
# class ChallengepAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'user', 'picture', 'post_at', 'mod_at')
