from rest_framework import permissions
from pprint import pprint

from rest_framework.permissions import SAFE_METHODS


class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


# for classes with user objects
class MeOrIsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        is_admin = super().has_permission(request, view)

        is_me = request.user.username == obj.user.username

        return is_me or is_admin


class IsMe(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.username == obj.username