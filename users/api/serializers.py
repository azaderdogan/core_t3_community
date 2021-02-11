from pprint import pprint

from rest_framework import serializers

from users.models import *


class FollowingSerializer(serializers.ModelSerializer):
    following_user = serializers.StringRelatedField()

    class Meta:
        model = UserFollowing
        lookup_field = 'username'
        fields = ('id', 'created_at', 'following_user')


class FollowersSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = UserFollowing
        lookup_field = 'username'
        fields = ('id', 'created_at', 'user')


class UserSerializer(serializers.ModelSerializer):
    followings = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', ]

        lookup_field = 'username'

    read_only_fields = ['id', 'create_date', 'update_date']

    def get_followings(self, object):
        following = object.following.all()
        # todo kullanıcıları usera cevir
        return FollowingSerializer(following, many=True).data

    def get_followers(self, object):
        followers = object.followers.all()
        return FollowersSerializer(followers, many=True).data


class RosetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rosette
        fields = '__all__'
        read_only_fields = ['id', 'create_date', 'update_date']


class RosetteForProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rosette
        fields = ['rosette_name']
        read_only_fields = ['id', 'create_date', 'update_date']


# user/username/profile
class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.HyperlinkedRelatedField(read_only=True, view_name="user-detail-detail")
    user = serializers.HyperlinkedRelatedField(read_only=True, view_name='users:user-detail', lookup_field='username')
    profile_photo = serializers.ImageField(read_only=True)
    rosettes = RosetteForProfileSerializer(many=True, read_only=True)
    city = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    school = serializers.StringRelatedField()
    faculty = serializers.StringRelatedField()
    department = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['id', 'create_date', 'update_date']

    def update(self, instance, validated_data):
        pprint(instance)


# /photo
class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_photo']


class RosetteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rosette
        fields = ['rosette_name']


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
