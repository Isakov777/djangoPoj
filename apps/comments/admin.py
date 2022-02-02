from django.contrib import admin
from apps.comments.models import Comment
from apps.posts.models import Post, PostImage, PostVideo, Tag
from apps.users.models import User


admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostVideo)
admin.site.register(PostImage)
admin.site.register(User)
admin.site.register(Tag)