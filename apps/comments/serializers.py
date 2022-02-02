from dataclasses import fields
from rest_framework import serializers
from apps.posts.models import Post 
from apps.users.models import User
from apps.comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):

    user = serializers.CharField(read_only = True)

    class Meta:

        model = Comment
        fields = '__all__'
        

        
