from rest_framework import permissions

class IsAdminOrReadCreateUpdateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.user.groups.filter(name='Manager').exists():
            return request.method in ['GET', 'POST', 'PUT', 'PATCH']
        return False