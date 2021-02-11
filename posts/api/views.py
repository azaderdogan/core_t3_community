from rest_framework import viewsets, status
from rest_framework.response import Response

from posts.models import *
from posts.api.serializers import *
from pprint import pprint
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, NotAcceptable
from rest_framework.generics import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        me = self.request.user
        pprint(me)
        serializer.save(author=me)

    @action(detail=True)
    def like(self, request, pk=None):
        user = request.user
        # todo id cek
        post = self.get_object()
        pprint(post)
        user_likes = Post.likes.get(username=user.username)
        if user_likes.exists():
            raise NotAcceptable('Daha önce beğenmiştiniz')


class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentSerializer

    def perform_create(self, serializer):
        parent_post_pk = self.kwargs.get('post_pk')
        parent_post = get_object_or_404(Post, pk=parent_post_pk)
        pprint(parent_post)

        me = self.request.user
        pprint('CALISTIIII')

        serializer.save(parent_post=parent_post, author=me)

    def get_queryset(self, *args, **kwargs):
        post_pk = self.kwargs.get('post_pk')
        post = Post.objects.get(pk=post_pk)
        comments = PostComment.objects.filter(parent_post=post)
        return comments


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
