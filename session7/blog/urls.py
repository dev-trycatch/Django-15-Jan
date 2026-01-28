from django.urls import path
from .views import *
urlpatterns = [
    path('CreateBlog/',CreateBlog,name = 'CreateBlog'),
    path('blogList/',blogList,name = 'blogList'),
]   