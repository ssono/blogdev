from django.contrib import admin
from .models import Post, Comment, News

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    ordering = ('-date',)

class CommentAdmin(admin.ModelAdmin):
    list_display =('parent_post', 'text')
    search_fields = ('parent_post',)
    ordering = ('parent_post',)

class NewsAdmin(admin.ModelAdmin):
    list_display =('title',)
    ordering =('-date',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)
#admin.site.register(Comment)#
# Register your models here.
