from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def CreateBlog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        img = request.FILES.get('img')

        Blog.objects.create(
            title = title,
            content = content,
            img = img
        )
        return redirect('/CreateBlog/')

    return render(request,'blogForm.html')


def blogList(request):
    search = request.GET.get('search')
    # print(search)
    blogs = Blog.objects.all().order_by('-created_at')

    if search:
        blogs = blogs.filter(Q(title__icontains=search) | Q(content__icontains=search))
        print(blogs)

    paginator = Paginator(blogs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        # 'blogs':blogs,
        'page_obj':page_obj
    }
    return render(request,'blogList.html',context)
