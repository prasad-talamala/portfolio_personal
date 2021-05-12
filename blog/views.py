from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('date')
    return render(request, "all_blogs.html", {"blogs": blogs})


def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "details.html", {"blog": blog})
