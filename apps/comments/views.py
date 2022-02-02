from django.shortcuts import render
from .serializers import CommentSerializer
from .models import Comment
from apps.posts.permissions import OwnerPostPermission
from rest_framework import viewsets


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [OwnerPostPermission]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)