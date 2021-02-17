from rest_framework import viewsets, status
from rest_framework.response import Response

from posts.models import *
from posts.api.serializers import *
from pprint import pprint
from rest_framework.decorators import action, permission_classes
from rest_framework.exceptions import NotFound, NotAcceptable
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from posts.api.permissions import IsPostAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    # todo queryseti takip ettiği kişilere göre ayarla
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostAuthorOrReadOnly]

    def perform_create(self, serializer):
        me = self.request.user
        pprint(me)
        serializer.save(author=me)

    @action(detail=True)
    def like(self, request, pk=None):
        user = request.user
        post = self.get_object()
        if post.likes.filter(username=user.username).exists():
            raise NotAcceptable('Daha önce beğenmiştiniz')
        user.post_likes.add(post)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True)
    def dislike(self, request, pk=None):
        user = request.user
        post = self.get_object()
        if post.likes.filter(username=user.username).exists() != True:
            raise NotAcceptable('Zaten beğenmemiştiniz')
        user.post_likes.remove(post)
        return Response(status=status.HTTP_200_OK)


class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentSerializer
    permission_classes = [IsPostAuthorOrReadOnly]

    def perform_create(self, serializer):
        parent_post_pk = self.kwargs.get('post_pk')
        parent_post = get_object_or_404(Post, pk=parent_post_pk)
        me = self.request.user

        serializer.save(parent_post=parent_post, author=me)

    def get_queryset(self, *args, **kwargs):
        post_pk = self.kwargs.get('post_pk')
        post = Post.objects.get(pk=post_pk)
        comments = PostComment.objects.filter(parent_post=post)
        return comments

    @action(detail=True)
    def like(self, request, pk=None, post_pk=None):
        user = request.user
        comment = self.get_object()
        if comment.likes.filter(username=user.username).exists():
            raise NotAcceptable('Daha önce beğenmiştiniz')
        user.comment_likes.add(comment)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True)
    def dislike(self, request, pk=None, post_pk=None):
        user = request.user
        comment = self.get_object()
        if not comment.likes.filter(username=user.username).exists():
            raise NotAcceptable('Zaten beğenmemiştiniz')
        user.comment_likes.remove(comment)
        return Response(status=status.HTTP_200_OK)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


"""{
    "activity_name": "Django etkinliği",
    "about": "Django hakkında etkinliğimiz olacaktır",
    "is_online": true,
    "is_private": false,
    "starting_date": "2021-02-13T16:30:00+03:00",
    "due_date": "2021-02-13T18:45:00+03:00",
    "broadcasting_url": "url",
}"""


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    lookup_field = 'slug'

    @action(detail=True, permission_classes=[IsAuthenticated])
    def join(self, request, slug=None, *args, **kwargs):
        activity = get_object_or_404(Activity, slug=slug)
        me = self.request.user
        if not activity.participants.filter(username=me.username).exists():
            activity.participants.add(me)
            return Response({'detail': 'Succesfully'})
        else:
            return Response({'detail': 'Zaten katılımcısınız'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, permission_classes=[IsAuthenticated])
    def non_join(self, request, slug=None, *args, **kwargs):
        activity = get_object_or_404(Activity, slug=slug)
        user = self.request.user
        participants = activity.participants.filter(username=user.username)
        if participants.exists():
            activity.participants.remove(self.request.user)
            return Response({'detail': 'Succesfully'})
        else:
            return Response({'detail': 'Zaten katılımcı değilsiniz'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, permission_classes=[IsAdminUser])
    def active(self, request, slug=None, *args, **kwargs):
        activity = get_object_or_404(Activity, slug=slug)
        if not activity.is_active:
            activity.is_active = True
            return Response({'detail': 'Etkinlik onaylandı'})
        else:
            return Response({'detail': 'Zaten onaylanmış'})
