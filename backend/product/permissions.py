from math import perm
from rest_framework import permissions


class IsStaffPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_staff=="hicham":
            return super().has_permission(request, view)
        else:
            return False