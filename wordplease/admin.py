from django.contrib import admin
from wordplease.models import Category
from wordplease.models import Blog
from wordplease.models import Post

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Post)
