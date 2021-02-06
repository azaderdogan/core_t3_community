from rest_framework import viewsets
from rest_framework import mixins
from users.models import *
from users.api.serializers import *
from rest_framework import generics
from rest_framework import permissions
from pprint import pprint


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# todo admin/users/profile/4/change/
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        profile_pk = self.kwargs.get('pk')
        profile = generics.get_object_or_404(Profile, pk=profile_pk)
        city = generics.get_object_or_404(City, city_name=self.request.data['city'])
        district = generics.get_object_or_404(District, city=city, district_name=self.request.data['district'])
        profile.city = city
        profile.district = district

        pprint(self.request.data)
        pprint(self.kwargs.get('pk'))
        serializer.save(city=city, district=district, rosettes=self.request.data['rosettes'], user=self.request.user)

    # def perform_update(self, serializer):
    #     profile = generics.get_object_or_404(Profile, pk=self.kwargs.get('pk'))
    #     user = self.request.user
    #     city = self.request.data['city']
    #     city_instance = City.objects.get(city_name=city)
    #     profile.city = city_instance
    #     serializer.save(profile=profile,user = user)


class ProfilePhotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilePhotoSerializer

    def get_object(self):
        profile = self.request.user.profile
        return profile


class RosetteListViewSet(viewsets.ModelViewSet):
    queryset = Rosette.objects.all()
    serializer_class = RosetteSerializer


class RosetteUpdateViewSet(generics.UpdateAPIView):
    serializer_class = RosetteSerializer
    queryset = Rosette.objects.all()
