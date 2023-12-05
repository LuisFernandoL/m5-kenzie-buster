from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsEmployeeOrReadyOnly(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        return (
            req.method in permissions.SAFE_METHODS
            or req.user.is_authenticated
            and req.user.is_superuser
        )


class IsUserAdmin(permissions.BasePermission):
    def has_object_permission(self, req: Request, view: View, obj: User):
        return obj == req.user or req.user.is_employee
