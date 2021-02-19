from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class Followers(models.Model):
    follower_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        db_table = 'followers'


class Following(models.Model):
    following_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        db_table = 'following'
