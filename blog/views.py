from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

# Create your views here.


def post_list(request):
    object_list = Post.published.all()
    page = request.GET.get('page')
    paginator = Paginator(object_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    total_published_post = object_list.count()
    return render(request, 'list.html', {'posts': posts, 'total_published_post': total_published_post})


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'details.html', {'post': post})
