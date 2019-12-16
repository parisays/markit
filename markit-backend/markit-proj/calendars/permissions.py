from rest_framework import permissions
from collaboration.models import Collaborator
from collaboration.consts import Access

# obj is a Calendar instance

class CalendarPermission(permissions.BasePermission):
    """
    Check calendar access.
    """
    SAFE_ACCESS = {
        'get':Access.VIEW_CALENDAR,
        'put':Access.EDIT_CALENDAR,
        'patch':Access.EDIT_CALENDAR,
        'delete':Access.DELETE_CALENDAR,
                }

    def has_object_permission(self, request, view, obj):
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj)
            for access in self.SAFE_ACCESS.get(request.method, []):
                if access not in collab.role.access:
                    return False
            return True
        except:
            return False

class UpdateCalendarPermission(permissions.BasePermission):
    """
    Check update calendar access.
    """
    SAFE_ACCESS = [Access.EDIT_CALENDAR]

    def has_object_permission(self, request, view, obj):
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj)
            for access in self.SAFE_ACCESS:
                if access not in collab.role.access:
                    return False
            return True
        except:
            return False


class DestroyCalendarPermission(permissions.BasePermission):
    """
    Check destroy calendar access.
    """
    SAFE_ACCESS = [Access.DELETE_CALENDAR]

    def has_object_permission(self, request, view, obj):
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj)
            for access in self.SAFE_ACCESS:
                if access not in collab.role.access:
                    return False
            return True
        except:
            return False


class RetrieveCalendarPermission(permissions.BasePermission):
    """
    Check retrieve calendar access.
    """
    SAFE_ACCESS = [Access.VIEW_CALENDAR]

    def has_object_permission(self, request, view, obj):
        try:
            collab = Collaborator.objects.filter(user=request.user).get(calendar=obj)
            for access in self.SAFE_ACCESS:
                if access not in collab.role.access:
                    return False
            return True
        except:
            return False
