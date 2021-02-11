from django.urls import path, include
from rest_framework.routers import SimpleRouter
from users.api.views import *
from rest_framework_nested import routers

# pip install drf-nested-routers

router = SimpleRouter()

router.register('users', UserViewSet)

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

#
# router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'rosettes', RosetteListViewSet, basename='rosette')
# router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('photo/', ProfilePhotoUpdateView.as_view()),
   # path('', include(profile_router.urls)),
    path('users/<str:username>/profile/', ProfileRetrieveViewSet.as_view()),

]
