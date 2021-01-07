from django.shortcuts import render, get_object_or_404
from .models import Blog

def allBlogs(request):
    blogs = Blog.objects.order_by("-date")[:5]
    return render(request, "blog/allBlogs.html",{"blogs":blogs})

def blogDetails(request, blog_id):
    blog = get_object_or_404(Blog,pk = blog_id)
    return render(request, "blog/blogDetails.html",{"blog": blog})
