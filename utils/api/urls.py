from django.urls import path, include
from rest_framework.routers import SimpleRouter
from utils.api.views import *
from rest_framework_nested import routers

school_router = SimpleRouter()
school_router.register(r'schools', SchoolListView, basename='school')

faculties_router = routers.NestedSimpleRouter(
    school_router,
    r'schools',
    lookup='school'
)
faculties_router.register(r'faculties',FacultyListView,basename='faculty')

departments_router = routers.NestedSimpleRouter(
    faculties_router,
    r'faculties',
    lookup='faculty'
)
departments_router.register(r'departments', DepartmentListView, basename='department')

city_router = SimpleRouter()
city_router.register(r'cities', CityListView, basename='city')

district_router = routers.NestedSimpleRouter(
    city_router,
    r'cities',
    lookup='city'
)
district_router.register(
    r'districts',
    DistrictListView,
    basename='city-district'
)

app_name = 'utils'
urlpatterns = [
    path('', include(city_router.urls)),
    path('', include(school_router.urls)),
    path('', include(district_router.urls)),
    path('', include(faculties_router.urls)),
    path('', include(departments_router.urls)),

]
