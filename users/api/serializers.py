from rest_framework import serializers

from users.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions', 'is_verified', 'is_active', 'is_staff']

    read_only_fields = ['id', 'create_date', 'update_date']


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
    user = UserSerializer(read_only=True)
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

    # def update(self, instance, validated_data):
    #     return instance
    #



# /photo
class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_photo']


class RosetteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rosette
        fields = ['rosette_name']
