from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
@admin.register(Blog)
class admin_b(admin.ModelAdmin):
    display_list = ['user', 'title']

@admin.register(Comment)
class comment_b(admin.ModelAdmin):
    list_display = ('user', 'body', 'blog', 'active')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)