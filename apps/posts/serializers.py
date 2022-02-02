from dataclasses import fields
from distutils import command
from rest_framework import serializers
from apps.posts.models import Post,  PostImage, Tag, Like, PostVideo
from apps.comments.serializers import CommentSerializer


class PostlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'




class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'




class PostImagseializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'



class PostVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = '__all__'

    

class PostSerializer(serializers.ModelSerializer):

    total_likes = serializers.SerializerMethodField()
    post_image = PostImagseializer(many = True, read_only = True)
    user = serializers.CharField(read_only = True)
    post_video = PostVideoSerializer(many = True, read_only = True)
    comment_post = CommentSerializer(many = True, read_only = True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_total_likes(self, instance):
        return instance.post_like.all().count()



class PostDetailSerializer(serializers.ModelSerializer):

    image = PostImagseializer(many = True, read_only = True)
    user = serializers.CharField(read_only = True)
    
    class Meta:
        model = Post
        fields = '__all__'






