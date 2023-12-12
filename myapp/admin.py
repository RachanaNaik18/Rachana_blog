from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class admin_b(admin.ModelAdmin):
    display_list = ['user', 'title']
