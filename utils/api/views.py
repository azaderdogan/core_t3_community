from rest_framework import viewsets, mixins
from utils.models import *
from utils.api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from pprint import pprint
from rest_framework import viewsets


class CityListView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class DistrictListView(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer

    def get_queryset(self, *args, **kwargs):
        city = get_object_or_404(City, pk=self.kwargs.get('city_pk'))
        print('Çalışıyor', city)
        queryset = District.objects.filter(city=city)
        return queryset


class SchoolListView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class FacultyListView(viewsets.ModelViewSet):
    serializer_class = FacultySerializer

    def get_queryset(self):
        school = get_object_or_404(School, pk=self.kwargs.get('school_pk'))
        queryset = Faculty.objects.filter(school=school)
        return queryset


class DepartmentListView(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        faculty = get_object_or_404(Faculty, pk=self.kwargs.get('faculty_pk'))
        queryset = Department.objects.filter(faculty=faculty)
        return queryset
