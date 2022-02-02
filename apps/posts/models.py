from distutils.command.upload import upload
from operator import mod
import re
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()




class Tag(models.Model):
    title = models.CharField(max_length=255, db_index=True, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self) -> str:
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')

    tags = models.ManyToManyField(Tag, related_name='post_tag')

    def __str__(self) -> str:
        return self.title



class PostImage(models.Model):
    image = models.ImageField(upload_to = 'post_image')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_image')

    def __str__(self) -> str:
        return self.post.title



class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,  related_name='post_like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self) -> str:
        return self.like.title


class PostVideo(models.Model):
    video = models.FileField(upload_to = 'video')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_video')

    def __str__(self) -> str:
        return self.post.title