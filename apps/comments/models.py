import imp
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model
from apps.posts.models import Post

User = get_user_model()


class Comment(models.Model):
    text = models.TextField(blank = True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comment_post')


    def str(self):
        return self.text