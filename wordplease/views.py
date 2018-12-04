from django.http import HttpResponse
from django.shortcuts import render
from wordplease.models import Post, Blog, User


def home(request):
    post_list = Post.objects.all().order_by('-published_time')

    post_context = {'Posts': post_list}

    return render(request, 'wordplease/home.html', post_context)


def blogs(request):
    blog_list = Blog.objects.all().order_by('creation_date')

    blog_context = {'Blogs': blog_list}
    return render(request, 'wordplease/blogs/home.html', blog_context)


def user_posts(request, username):
    try:
        _posts_ids = []
        _user = User.objects.get(username=username)
        user_posts_list = Blog.objects.values('post').filter(pk=_user.id).order_by('creation_date')

        for _post in user_posts_list:
            if _post.get('post'):
                _posts_ids.append(_post.get('post'))
            elif not _post.get('post') and len(user_posts_list) is 1:
                return render(request, 'wordplease/posts/no_post.html')
        posts = Post.objects.all().filter(pk__in=_posts_ids)
        post_context = {'Posts': posts}

        return render(request, 'wordplease/Blogs/user_posts.html', post_context)
    except User.DoesNotExist:
        return HttpResponse('User not found', status=404)


def post(request, username, post_id):
    try:
        _post = Post.objects.get(pk=post_id)
        post_context = {'Post': _post}
        return render(request, 'wordplease/posts/post.html', post_context)
    except Post.DoesNotExist:
        return HttpResponse('Post not found', status=404)

