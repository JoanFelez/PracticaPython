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
        _user = User.objects.values('id').filter(username=username)
        user_posts_list = Blog.objects.values('post').filter(user_id=_user[0].get('id')).order_by('creation_date')
        for post in user_posts_list:
            if post.get('post'):
                _posts_ids.append(post.get('post'))
        posts = Post.objects.all().filter(id__in=_posts_ids)
        post_context = {'Posts': posts}

        return render(request, 'wordplease/Blogs/user_posts.html', post_context)
    except User.DoesNotExist:
        return HttpResponse('User not found', status=404)
