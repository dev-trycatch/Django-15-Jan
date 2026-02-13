from django.shortcuts import render
from django.core.cache import cache
from .models import *
from django.views.decorators.cache import cache_page

# Create your views here.

# 1. locMem cache

# def post_list(request):
#     posts = cache.get('all_posts')
#     if not posts:
#         print('Fetching Data from Database')
#         posts = Post.objects.all()
#         cache.set('all_posts',posts,timeout=60)
#     else:
#         print('Fetching Data from locMem cache')
#     return render(request,'all_list.html',{'posts':posts})









# 2. file based cache
# def post_list_file(request):
#     posts = cache.get('all_posts')
#     if not posts:
#         print('Fetching Data from Database')
#         posts = Post.objects.all()
#         cache.set('all_posts',posts,timeout=60)
#     else:
#         print('Fetching Data from File based cache')
#     return render(request,'all_list.html',{'posts':posts})


# 3. database cache

# def post_list_database(request):
#     posts = cache.get('all_posts')
#     if not posts:
#         print('Fetching Data from Database')
#         posts = Post.objects.all()
#         cache.set('all_posts',posts,timeout=60)
#     else:
#         print('Fetching Data from Database cache')
#     return render(request,'all_list.html',{'posts':posts})




# 4. template fragment cache

def post_list(request):
    posts = Post.objects.all()
    return render(request,'post_list.html',{'posts':posts})

# 5. per view cache
# @cache_page(10)
# def post_list_file(request):
#     posts = cache.get('all_posts')
#     if not posts:
#         print('Fetching Data from Database')
#         posts = Post.objects.all()
#         cache.set('all_posts',posts,timeout=60)
#     else:
#         print('Fetching Data from File based cache')
#     return render(request,'all_list.html',{'posts':posts})

# 6.external cache

