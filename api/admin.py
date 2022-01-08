from django.contrib import admin
from .models import Post, Group, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pub_date', 'author', 'group')
    empty_value_display = '-empty-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'slug')
    empty_value_display = '-empty-'
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'post', 'text', 'created')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'user')


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
