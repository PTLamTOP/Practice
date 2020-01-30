from django.db import models
from django.conf import settings
from posts.models import Post


class View(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='views')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='views')
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post}-{self.views_count}"
