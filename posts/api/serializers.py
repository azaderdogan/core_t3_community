from django.contrib.sites.models import Site
from rest_framework import serializers
from posts.models import *
from users.api.serializers import UserSerializer
from datetime import datetime, date
from django.utils.timesince import timesince


class PostCommentSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='users:user-detail',
        lookup_field='username'
    )
    tags = serializers.StringRelatedField(many=True, read_only=True)
    time_since_pub = serializers.SerializerMethodField()
    parent_post = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='posts:post-detail',
        lookup_field='pk'
    )
    number_of_likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PostComment
        fields = '__all__'

        read_only_fields = ['likes']

    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.create_date
        time_delta = timesince(pub_date, now)

        return time_delta

    def get_number_of_likes(self, obj):
        count = obj.likes.count()
        return count


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='users:user-detail',
        lookup_field='username'
    )
    time_since_pub = serializers.SerializerMethodField()
    comments = serializers.StringRelatedField(read_only=True, many=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    number_of_likes = serializers.SerializerMethodField(read_only=True)
    likes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['likes']

    def get_time_since_pub(self, object):
        now = datetime.now()
        pub_date = object.create_date
        time_delta = timesince(pub_date, now)

        return time_delta

    def get_number_of_likes(self, obj):
        print('BURASI PATLADI')
        count = obj.likes.count()
        return count


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    creator = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='users:user-detail',
        lookup_field='username'
    )
    slug = serializers.SlugRelatedField(
        slug_field='slug',
        read_only=True
    )

    class Meta:
        model = Activity
        fields = '__all__'
        lookup_field = 'slug'
        read_only_fields = ['slug', 'is_active']

    def get_slug(self, obj):
        return f'http://127.0.0.1:8000/api/actions/activities/{obj.slug}/'


class ActivityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        lookup_field = 'slug'
        read_only_fields = ['slug', 'is_active']
