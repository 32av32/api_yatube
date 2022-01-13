from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name='Text')
    pub_date = models.DateTimeField(verbose_name='Date of publish', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Author')
    group = models.ForeignKey('Group', blank=True, null=True, verbose_name='Group', on_delete=models.CASCADE,
                              related_name='posts')

    def __str__(self):
        return self.text


class Group(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Post')
    text = models.TextField(verbose_name='Text')
    created = models.DateTimeField(verbose_name='Date of create', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower', verbose_name='User')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', verbose_name='Following')

    class Meta:
        unique_together = ['user', 'following']
