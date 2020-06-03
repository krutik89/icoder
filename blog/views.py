from django.shortcuts import render,HttpResponse
from .models import Blog
# Create your views here.
def blog(request):
    allPosts = Blog.objects.all()
    context = {'allPosts':allPosts}
    return render(request,'blog/blog.html',context)
def blogpost(request,slug):
    posts = Blog.objects.filter(slug=slug).first()
    context = {'post':posts}
    return render(request,'blog/blogpost.html',context)