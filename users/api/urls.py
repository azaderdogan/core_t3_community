from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api.views import *
router = DefaultRouter()

router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'rosettes', RosetteListViewSet, basename='rosette')
router.register(r'',UserViewSet,basename='user')
users_list_view = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
urlpatterns = [
    path('', include(router.urls)),
    path('photo/', ProfilePhotoUpdateView.as_view()),
    #path('rosette/', RosetteUpdateViewSet.as_view()),

    # path('profiles/', ),
    # path('profiles/<int:pk>/', ),
    # path('cities/', name='sehirler'),
    # path('cities/<int:pk>/', name='ilceler'),
    # path('university/', name='universiteler'),
    # path('university/<int:pk>/', name='fakulteler'),
    # path('university/<int:pk>/<int:pk>/', name='bolumler'),
    # path('users/<int:pk>/', ProfileViewSet.as_view({'get': 'list'}))
    # path('users/<int:pk>/', UserListCreateAPIView.as_view(), name='users'),

]
