from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
# Create your models here.


class Movies(models.Model):
    img_url = models.CharField(max_length=255)
    movie_id = models.CharField(max_length=255)
    movie_type_list = models.JSONField()
    movie_regions_list = models.JSONField()
    movie_title = models.CharField(max_length=255)
    movie_url = models.CharField(max_length=255)
    movie_score = models.CharField(max_length=255)
    release_time = models.CharField(max_length=255, null=True, blank=True)
    actor_count = models.CharField(max_length=255)
    vote_count = models.CharField(max_length=255)
    actor_list = models.JSONField()
    introduction = models.TextField(null=True)
    trailer_url = models.CharField(max_length=255, null=True)
    comment_list = models.JSONField(null=True)
    score = models.FloatField(default=0)
    assess_count = models.IntegerField(default=0)


class Details(models.Model):
    video_url = models.CharField(max_length=255)
    introduction = models.TextField()
    movie_title = models.CharField(max_length=255)
    comment = models.JSONField()


class Test(models.Model):
    video_url = models.CharField(max_length=255)
    introduction = models.TextField()
    movie_title = models.CharField(max_length=255)
    comment = models.JSONField()


class NewUser(AbstractUser):
    favor_tags = models.JSONField(null=True)
    favor_movies = models.JSONField(null=True)
    photo = models.URLField(null=True)

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        pass

