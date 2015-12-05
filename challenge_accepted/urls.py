"""challenge_accepted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from api.views import APIListCreateChallengev, APIDetailUpdateChallengev, APIListCreateLike, APIDetailUpdateLike, \
    APIListCreateSubmissionv, APIDetailUpdateSubmissionv
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/challengev/$', APIListCreateChallengev.as_view(), name='api_challenge_list'),
    url(r'^api/challengev/(?P<pk>\d+)$', APIDetailUpdateChallengev.as_view(), name='api_challenge_detail'),
    url(r'^api/submissionv/$', APIListCreateSubmissionv.as_view(), name='api_list'),
    url(r'^api/submissionv/(?P<pk>\d+)$', APIDetailUpdateSubmissionv.as_view(), name='api_detail'),
    url(r'^api/like/$', APIListCreateLike.as_view(), name='like_list'),
    url(r'^api/like/(?P<pk>\d+)$', APIDetailUpdateLike.as_view(), name='like_detial'),
]
