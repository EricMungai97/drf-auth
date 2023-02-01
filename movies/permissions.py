from rest_framework import permissions


# https://www.django-rest-framework.org/api-guide/permissions/#examples
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.owner is None:
            return True

        return obj.owner == request.user
