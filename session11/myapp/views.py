from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'post_form.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','content']
    template_name = 'post_form.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete_confirm.html'
    success_url = reverse_lazy('post-list')
    