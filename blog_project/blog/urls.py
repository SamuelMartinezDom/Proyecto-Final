#blog/urls.py

from django.urls import path
from blog.views import BlogListView, BlogDetailView, new_blog

app_name = 'blog'

urlpatterns = [
    #post views
    path('', BlogListView.as_view(), name='blog_list'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new-blog/', new_blog, name='new_blog')
]