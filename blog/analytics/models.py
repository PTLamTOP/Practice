from django.db import models
from django.conf import settings
from posts.models import Post


class View(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post}-{self.views_count}"
