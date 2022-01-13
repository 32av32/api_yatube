from django.contrib import admin
from .models import Post, Group, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pub_date', 'author', 'group')
    empty_value_display = '-empty-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description',)
    empty_value_display = '-empty-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'post', 'text', 'created')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'following', 'user')


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
