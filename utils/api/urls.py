from django.urls import path, include
from rest_framework.routers import SimpleRouter
from utils.api.views import *
from rest_framework_nested import routers

router = SimpleRouter()

router.register(r'cities', CityListView, basename='city')

district_router = routers.NestedSimpleRouter(
    router,
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
    path('', include(router.urls)),
    path('', include(district_router.urls))
    # path('', include(router.urls)),
    # path('cities/', CityListView.as_view({'get': 'list'})),
    # path('cities/<int:pk>/', DistrictListView.as_view({'get': 'list'})),
    # path('schools/', SchoolListView.as_view({'get': 'list'})),
    # path('schools/<int:school_pk>/', FacultyListView.as_view({'get': 'list'})),
    # path('schools/<int:city_pk>/<int:faculty_pk>/', DepartmentListView.as_view({'get': 'list'})),
    #
]
