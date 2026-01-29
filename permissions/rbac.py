from rest_framework.permissions import BasePermission

class IsAdminOrRequester(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ["Admin", "Requester"]
