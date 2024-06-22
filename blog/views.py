from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

class BlogHome(ListView):
    model = Post
    template_name = 'blog.html'

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})