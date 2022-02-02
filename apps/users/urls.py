from django import views
from django.urls import path
from unicodedata import name
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewSet

from apps.comments.views import CommentViewSet
from apps.posts.views import PostViewSet, PostImageViewSet, PostLikeViewSet, PostTagViewSet, PostVideoViewSet


router = DefaultRouter()

router.register('users', UserViewSet)
router.register('post', PostViewSet)
router.register('post_image', PostImageViewSet)

router.register('post_video', PostVideoViewSet, basename='post_video_api')
router.register('tags', PostTagViewSet, basename='post_tag_api')
router.register('comments', CommentViewSet, basename='comment_api')


urlpatterns = [
    path('like/', PostLikeViewSet.as_view()),

]


urlpatterns += router.urls