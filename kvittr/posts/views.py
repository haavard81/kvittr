from django.http import Http404
from django.shortcuts import render_to_response
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


def post_details(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        posts = Post.objects.all()
        context = {'post': post}
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'posts/post_details.html', context)    


@login_required
def post_add_likes(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.likes = post.likes + 1
    post.save()
    data = {'likes_updated': post.likes}
    return JsonResponse(data)
    