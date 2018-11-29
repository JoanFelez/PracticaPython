from django.contrib.auth.models import User
from django.db import models


#Category Model
class Category(models.Model):
    name = models.CharField(max_length=20)

#Post Model
class Post(models.Model):

    title = models.CharField(max_length=150)
    introduction = models.TextField(default='The Introduction of the Post')
    text = models.TextField()
    image = models.FileField()
    categories = models.ManyToManyField(Category)
    published_time = models.DateTimeField(auto_now_add=True)

#Blog Model
class Blog(models.Model):
    title = models.CharField(max_length=150)
    creation_date = models.DateField(auto_now_add=True, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)


