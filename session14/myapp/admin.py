from django.contrib import admin
from .models import *
from django.core.cache import cache
from django.contrib import messages

@admin.action(description='Clear post cache')
def clear_cache_post(modelAdmin,request,queryset):
    cache.delete('all_posts')
    messages.success(request,'Cache clear successfully')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content']
    actions = [clear_cache_post]
