from django.urls import path, include
from rest_framework.routers import SimpleRouter
from users.api.views import *
from rest_framework_nested import routers

# pip install drf-nested-routers

parent_router = SimpleRouter()

parent_router.register('users', UserViewSet,basename='user')

# profile_router = routers.NestedSimpleRouter(
#     router,
#     r'users',
#     lookup='user'
# )
#
# profile_router.register(
#     r'profile',
#     ProfileViewSet,
#     basename='user-profile',
# )

app_name = 'users'

parent_router.register(r'rosettes', RosetteViewSet, basename='rosette')

urlpatterns = [
    path('', include(parent_router.urls)),
    path('photo/', ProfilePhotoUpdateView.as_view()),
    # path('', include(profile_router.urls)),
    path('users/<str:username>/profile/', ProfileRetrieveViewSet.as_view()),

]
