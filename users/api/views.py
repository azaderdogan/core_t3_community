from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAcceptable
from rest_framework.decorators import action
from users.api.serializers import *
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from pprint import pprint

from rest_framework.generics import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    @action(detail=True)
    def follow(self, request, username=None, *args, **kwargs):
        username = self.kwargs.get('username')
        user = User.objects.get(username=username)
        me = request.user
        my_followings = me.following.all()
        if user is None:
            raise NotFound('Böyle bir kullanıcı bulunamadı')
        elif user.username == me.username:
            raise NotAcceptable('Kişi kendini takip edemez!')
        elif my_followings.exists():
            raise NotAcceptable('Zaten takip ediyorsunuz')
        else:
            UserFollowing.objects.create(user=me, following_user=user)

        return Response(status=status.HTTP_200_OK)

    @action(detail=True)
    def unfollow(self, request, username=None, *args, **kwargs):
        print('Takipten çıkarılıyor')
        username = self.kwargs.get('username')
        user = User.objects.get(username=username)
        me = request.user
        followings = me.following.filter(following_user=user)

        if user is None:
            raise NotFound('Böyle bir kullanıcı bulunamadı')
        elif user.username == me.username:
            raise NotAcceptable('Kişi kendini takip edemez!')
        elif followings.exists() != True:
            raise NotAcceptable('Zaten takip etmiyorsunuz')
        else:
            print('Cıkartılacak')
            user_following = get_object_or_404(UserFollowing, user=me, following_user=user)

            user_following.delete()

        return Response(status=status.HTTP_200_OK)


# todo admin/users/profile/4/change/
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        pprint('GİRİLDİ')
        profile_pk = self.kwargs.get('pk')
        profile = generics.get_object_or_404(Profile, pk=profile_pk)
        city = generics.get_object_or_404(City, city_name=self.request.data['city'])
        district = generics.get_object_or_404(District, city=city, district_name=self.request.data['district'])
        profile.city = city
        profile.district = district

        pprint(self.request.data)
        pprint(self.kwargs.get('pk'))
        serializer.save(city=city, district=district, rosettes=self.request.data['rosettes'], user=self.request.user)

    def get_queryset(self, *args, **kwargs):

        username = self.kwargs.get('user_username')

        try:
            user = User.objects.get_by_natural_key(username=username)
        except User.DoesNotExist:
            raise NotFound('Böyle bir kullanıcı bulunamadı')
        return self.queryset.filter(user=user)


class ProfilePhotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilePhotoSerializer

    def get_object(self):
        profile = self.request.user.profile
        return profile


class RosetteViewSet(viewsets.ModelViewSet):
    queryset = Rosette.objects.all()
    serializer_class = RosetteSerializer

    @action(detail=True)
    def add_user(self, request, pk=None, *args, **kwargs):
        rosette = self.get_object()
        print(str(rosette))
        me = self.request.user
        me.profile.rosettes.add(rosette)
        # rosette.users.add(me_profile)
        return Response(status=status.HTTP_200_OK)


class ProfileRetrieveViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, *args, **kwargs):

        username = self.kwargs.get('username')

        try:
            user = User.objects.get_by_natural_key(username=username)
            profile = Profile.objects.get(user=user)
        except User.DoesNotExist:
            raise NotFound('Böyle bir kullanıcı bulunamadı')
        return profile

    """:return{
        "biography": "Milli Teknoloji Neferi",
        "birth_of_date": null,
        "phone_number": "054546656546",
        "tc_number": "39710000",
        "school": 1,
        "faculty": 1,
        "department": 16729,
        "city": 25,
        "district": 1
    }"""

    def update(self, request, *args, **kwargs):

        instance = self.get_object()
        serializer = ProfileUpdateSerializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors)

    def perform_update(self, serializer):
        me = self.request.user
        serializer.save(user=me)
