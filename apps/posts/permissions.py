from rest_framework.permissions import BasePermission


class IsPostOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return obj.author_name == request.user