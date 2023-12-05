from rest_framework import permissions
from rest_framework.views import Request, View


class IsEmployeeOrReadyOnly(permissions.BasePermission):
    def has_permission(self, req: Request, view: View):
        if req.method in permissions.SAFE_METHODS:
            return True
        if req.user.is_authenticated and req.user.is_superuser:
            return True
        return False        
