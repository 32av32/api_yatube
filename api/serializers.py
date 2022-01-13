from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post, Comment, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    following = serializers.SlugRelatedField(slug_field='username', queryset=get_user_model().objects.all())

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['author'] = instance.author.username
    #     return representation

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow
