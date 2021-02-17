from django.urls import path, include

from posts.api.views import *
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

parent_router = SimpleRouter()
activity_router = DefaultRouter()
activity_router.register(r'^activities', ActivityViewSet, basename='activity')

parent_router.register(r'', PostViewSet)
comment_router = routers.NestedSimpleRouter(
    parent_router,
    r'',
    lookup='post'
)

comment_router.register(
    r'comments',
    PostCommentViewSet,
    basename='comments',
)

app_name = 'posts'

urlpatterns = [

    path('posts/', include(parent_router.urls)),
    path('', include(comment_router.urls)),
    path('', include(activity_router.urls)),
   # path('activities/<str:slug>/', ActivityViewSet.as_view({'get': 'retrieve'}),name='xxactivity-detail')

]
