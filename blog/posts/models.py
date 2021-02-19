# Packages
from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class Posts(models.Model):
    content = models.CharField(max_length=1000)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    image = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        db_table = 'posts'
