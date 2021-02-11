from rest_framework import serializers
from utils.models import *


class CitySerializer(serializers.ModelSerializer):
    # districts = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = '__all__'

    def get_districts(self, obj):
        queryset = District.objects.filter(city=obj)
        serializer = DistrictSerializer(many=True, data=queryset)
        serializer.is_valid()
        lookup_field = 'plate_code'
        return serializer.data


class DistrictSerializer(serializers.ModelSerializer):
    # city = CitySerializer(read_only=True)
    class Meta:
        model = District
        fields = '__all__'


class CityDetailSerializer(serializers.ModelSerializer):
    # districts = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = '__all__'
    #
    # def get_districts(self, obj):
    #     queryset = District.objects.filter(city=obj)
    #     serializer = DistrictSerializer(many=True, data=queryset)
    #     serializer.is_valid()
    #     return serializer.data


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
