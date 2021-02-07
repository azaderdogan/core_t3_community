from django.db import models
from users.models import *


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200)
    number_of_uses = models.IntegerField(default=0)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name





""" class Answer(Model):
        question = ForeignKey(Question, related_name='answers', **kw)

    Question.answers.all()"""


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    number_of_likes = models.IntegerField(default=0)

    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.content.split()[0]


class PostComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    number_of_likes = models.IntegerField(default=0)

    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    tags = models.ManyToManyField(Tag, related_name='comments')
