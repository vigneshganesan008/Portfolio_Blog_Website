from django.shortcuts import render
from .models import Blog

def allBlogs(request):
    blogs = Blog.objects.order_by("-date")[:5]
    return render(request, "blog/allBlogs.html",{"blogs":blogs})
