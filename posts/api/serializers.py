from rest_framework import serializers
from posts.models import *
from users.api.serializers import UserSerializer
from datetime import datetime, date
from django.utils.timesince import timesince


class PostCommentSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )
    tags = serializers.StringRelatedField(many=True, read_only=True)
    parent_post = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='post-detail'
    )
    class Meta:
        model = PostComment
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    )
    time_since_pub = serializers.SerializerMethodField()
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail'
    )
    tags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.create_date
        time_delta = timesince(pub_date, now)

        return time_delta
