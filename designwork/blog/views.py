from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog_page(request):
    blogs = Blog.objects
    return render(request, 'blog.html' ,{'blog':blogs})

def blog_contant(request,blog_id):
    blogc = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_contant.html', {'blogc':blogc})
