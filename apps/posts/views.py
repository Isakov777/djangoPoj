
from django.http import request
from rest_framework import viewsets, generics
from apps.posts.serializers import PostSerializer, PostImagseializer, PostDetailSerializer, PostVideoSerializer, PostTagSerializer, PostlikeSerializer
from apps.posts.models import Post, PostImage, PostVideo, Tag, Like
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from apps.posts.permissions import OwnerPostPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [OwnerPostPermission, IsAuthenticatedOrReadOnly]


    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return PostDetailSerializer
        return self.serializer_class


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


    

class PostImageViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostImagseializer
    permission_classes = [OwnerPostPermission, IsAuthenticatedOrReadOnly]


class PostVideoViewSet(viewsets.ModelViewSet):
    queryset = PostVideo.objects.all()
    serializer_class = PostVideoSerializer
    permission_classes = [OwnerPostPermission, IsAuthenticatedOrReadOnly]


class PostTagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = PostTagSerializer
    permission_classes = [permissions.IsAdminUser]



class PostLikeViewSet(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = PostlikeSerializer
    permission_classes = [OwnerPostPermission, IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



