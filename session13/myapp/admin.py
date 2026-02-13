from django.contrib import admin
from .models import *

# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','content','created_at']
