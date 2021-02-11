from django.urls import path, include

from posts.api.views import *
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

parent_router = SimpleRouter()

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

# router = DefaultRouter()
# router.register(r'posts', PostViewSet, basename='post')
# router.register(r'comments', PostCommentViewSet, basename='comment')
# router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [

    path('', include(parent_router.urls)),
    path('', include(comment_router.urls)),

]
