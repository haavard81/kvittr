from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from posts.models import Post

def post_listing(request):

    if request.method == 'POST':
        new_post = request.POST.get('new_post')
        if new_post:
            post = Post()
            post.message = new_post
            post.created_datetime = timezone.now()
            post.created_by = request.user
            post.save()

    posts = Post.objects.all()
    #posts = Post.objects.filter().order_by('-likes')
    page = request.GET.get('page')
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        }
    return render(request, 'posts/post_listing.html', context)