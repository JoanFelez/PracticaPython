from django.http import HttpResponse
from django.shortcuts import render
from wordplease.models import Post, Blog, User


def home(request):
    post_list = Post.objects.all().select_related('user').order_by('-published_time')

    post_context = {'Posts': post_list}

    return render(request, 'wordplease/home.html', post_context)


def blogs(request):
    blog_list = Blog.objects.all().order_by('creation_date')

    blog_context = {'Blogs': blog_list}
    return render(request, 'wordplease/blogs/home.html', blog_context)


def _user_posts(request, username):
    try:
        _user = User.objects.get(username=username)
        _blog = Blog.objects.get(user=_user.pk)
        user_posts_list = list(Post.objects.all().select_related('user').filter(blog_id=_blog.pk).order_by('published_time'))

        return user_posts_list
    except User.DoesNotExist:
        return HttpResponse('User not found', status=404)


def user_posts(request, username):

        user_posts_list = _user_posts(request, username)

        if type(user_posts_list) is HttpResponse:
            return user_posts_list

        if len(user_posts_list) is 0:
                return render(request, 'wordplease/posts/no_post.html')

        post_context = {'Posts': user_posts_list}

        return render(request, 'wordplease/Blogs/user_posts.html', post_context)


def post(request, username, post_id):

    _post_list = _user_posts(request, username)

    if type(_post_list) is HttpResponse:
        return _post_list

    for _post in _post_list:
        if _post.pk == post_id:
            post_context = {'Post': _post}
            return render(request, 'wordplease/posts/post.html', post_context)

    return HttpResponse('Post not found', status=404)

