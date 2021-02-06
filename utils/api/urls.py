from django.urls import path, include
from rest_framework.routers import DefaultRouter
from utils.api.views import *

router = DefaultRouter()

router.register(r'cities', CityListView, basename='city')

urlpatterns = [
    path('', include(router.urls)),
    path('cities/', CityListView.as_view({'get': 'list'})),
    path('cities/<int:pk>/', DistrictListView.as_view({'get': 'list'})),
    path('schools/', SchoolListView.as_view({'get': 'list'})),
    path('schools/<int:school_pk>/', FacultyListView.as_view({'get': 'list'})),
    path('schools/<int:pk1>/<int:faculty_pk>/', DepartmentListView.as_view({'get': 'list'})),
]
