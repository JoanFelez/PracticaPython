from django.contrib.auth.models import User
from django.db import models


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return '%s' % self.name


# Post Model
class Post(models.Model):
    title = models.CharField(max_length=150)
    introduction = models.TextField(default='The Introduction of the Post')
    text = models.TextField()
    image = models.FileField()
    categories = models.ManyToManyField(Category)
    published_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.title


# Blog Model
class Blog(models.Model):
    title = models.CharField(max_length=150)
    creation_date = models.DateField(auto_now_add=True, editable=False)
    post = models.ManyToManyField(Post, blank=True)
    published_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, editable=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title
