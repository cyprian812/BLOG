from rest_framework.permissions import BasePermission
from models import admin

class IsAdminUser(BasePermission):
    def has_permission(self, request, view,obj):
        # Check if the user is authenticated and has the is_admin_user attribute set to True
        return request.user.is_authenticated and getattr(request.user, 'is_adminuser', False)

# class isstaff(BasePermission):
#     def has_object_permission(self, request, view,):
#         return super().has_object_permission(request, view, )


class isstaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user,'is_staffuser',False)


