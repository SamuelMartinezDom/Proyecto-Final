from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog_detail.html'

def new_blog(request):
    print(request.method)
    if request.method =='POST':
        print(request.POST)
    return render(request, 'blog/new_blog.html', context={})
