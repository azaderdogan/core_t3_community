import random
import string

from django.db import models
from django.utils.text import slugify

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')

    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='post_likes')

    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.content.split()[0]


class PostComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='comment_likes')

    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    tags = models.ManyToManyField(Tag, related_name='comments')

    def __str__(self):
        return self.content


class Activity(models.Model):
    creator = models.ForeignKey(User, related_name='activites', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, blank=True, related_name='activities_i_participatied_in')
    activity_name = models.CharField(max_length=255, null=False, blank=False)
    about = models.TextField(null=False)
    is_online = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    starting_date = models.DateTimeField(null=False)
    due_date = models.DateTimeField(null=False)
    broadcasting_url = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.activity_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.activity_name
